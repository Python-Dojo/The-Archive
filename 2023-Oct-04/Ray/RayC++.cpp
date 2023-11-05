// REQUIRES C++17 OR GREATER! 

// Got values of 8.71118e-05x^2 + 1.80022x + 31.8021 after 10000 itterations 
// Correct values are      0x^2 + 1.8    x + 32

#include <algorithm> //for std::sort
#include <array>
#include <cmath>    //for NAN
#include <cmath>    // for std::abs
#include <iostream> //for debuging
#include <stdlib.h> /* srand, rand */
#include <string>
#include <time.h> /* time for seed */

double inline tansig(const double input) {
  return (2 / (1 + exp(-2 * input))) - 1;
}

static constexpr const std::array<std::array<double, 2>, 10000> PopulateData() {
  constexpr std::array<double, 20000> unprocessedData = {
  // data must be comma seperated values AND have a comma at the end of each line 
#include "data.txt"
  };

  std::array<std::array<double, 2>, 10000> processedData;
  
  int i = 0;
  for (auto& pair : processedData) {
	  pair[0] = unprocessedData[i++];
	  pair[1] = unprocessedData[i++];
  }

  return processedData;
}


constexpr std::array<std::array<double, 2>, 10000> DATA = PopulateData();

namespace machineLearning {

enum class Score_method { Per_term, Rms, Worst_guess };
// 
constexpr int ORGANISMS_PER_GEN = 90;
constexpr Score_method SCORE_METHOD = Score_method::Per_term;
const int NUM_CHILD = 3;
const double DIV = RAND_MAX / 10;
const int DF = 15;

class organism {
private:
  double CalculateTerm(double term, double term_Score) {
    double delta = double((double)rand() / RAND_MAX) * ((2 * (rand() % 2)) - 1);

    delta *= scale * tansig(1.5 * term) * term_Score;
    return term + delta;
  }
  double scale = NAN;

public:
  double x1;
  double x2;
  double c;
  double score[4]; // general, x2, x1, c
  organism(double _x2, double _x1, double _c) {
    score[0] = -1;
    score[1] = 1;
    score[2] = 1;
    score[3] = 1;
    x1 = _x1;
    x2 = _x2;
    c = _c;
  }
  organism() {
    score[0] = -1;
    score[1] = 1;
    score[2] = 1;
    score[3] = 1;
    x1 = (rand() / DIV);
    x2 = (rand() / DIV);
    c = (rand() / DIV);
  }
	
  double makeGuess(double celsius) {
    return x2 * celsius * celsius + x1 * celsius + c;
  }

  organism reproduce(int index) {
    scale = ((double)(index + 1.0) / ORGANISMS_PER_GEN) * (score[0] / DF);
    // std::cout << scale << " = scale\n";
    return organism(CalculateTerm(x2, score[1]), CalculateTerm(x1, score[2]),
                    CalculateTerm(c, score[3]));
  }

  void SetScore() {
    if ((score[0]) == -1) {
      int len = (sizeof DATA / sizeof DATA[0]);
      switch (SCORE_METHOD) {
      case Score_method::Per_term: {
        int Catch = 0;
        for (auto pair : DATA) {
          if (pair[0] == 0) {
            Catch += 1;
            continue;
          }
          double f = (pair[1] - c) / pair[0]; // cached for efficency (y-c/x)
          score[1] += std::abs(((1 / pair[0]) * (f - x1)) - x2);
          score[2] += std::abs(f - (x2 * pair[0]) - x1);
          score[3] += std::abs(pair[1] - (pair[0] * ((x2 * pair[0]) + x1)) - c);
        }
        len -= Catch;
        score[1] = score[1] / len;
        score[2] = score[2] / len;
        score[3] = score[3] / len;
        score[0] = (score[1] + score[2] + score[3]);
        break;
      }
      case Score_method::Rms: {
        double total = 0;
        for (auto pair : DATA) {
          double s = pair[1] - makeGuess(pair[0]);
          total += s * s;
        }
        score[0] = sqrt(total) / len;
        break;
      }
      case Score_method::Worst_guess: {
        double score_ = 0;
        double worstGuess = 0;
        for (auto pair : DATA)
          score_ = pair[1] - makeGuess(pair[0]);
        worstGuess = (score_ > worstGuess) ? score_ : worstGuess;
        break;
      }
      } // end switch
    }   // end if
  }



  // needed for sort
  bool operator<(const organism &i) const { return (score[0] < i.score[0]); }

}; // end class

int generation = 0;

std::array<organism, (ORGANISMS_PER_GEN * NUM_CHILD)> genetic_pool;

void init() {
  srand(time(NULL));
  for (auto x : genetic_pool) {
    x = organism(); // init with random terms (-10 to 10, min/max determined by
                    // DIV)
  }
}

organism simulate_generation() {
  constexpr bool PRINT_GEN_INFO = true;
  constexpr size_t MOVING_AVERAGE_LENGTH = 10;
  double movingAvg[MOVING_AVERAGE_LENGTH];
  double AvgScore = 0;
  for (auto &spec : genetic_pool) {
    spec.SetScore();
    if (PRINT_GEN_INFO) {
      AvgScore += spec.score[0];
    }
  }
  if (PRINT_GEN_INFO) {
    AvgScore /= (ORGANISMS_PER_GEN * NUM_CHILD); // length of genpool
    movingAvg[(generation % MOVING_AVERAGE_LENGTH)] = AvgScore;
    double T = 0;
    for (auto A : movingAvg) {
      T += A;
    }
    T /= MOVING_AVERAGE_LENGTH;
    double Delta = T - AvgScore;
    std::cout << "Average=" << AvgScore << "   delta=" << Delta
              << "  gen=" << (double)generation << std::endl;
  }

  std::sort(genetic_pool.begin(), genetic_pool.end());

	const organism best = genetic_pool[0];
	
  for (int i = 0; i < ORGANISMS_PER_GEN; i++) {
    for (int ii = (NUM_CHILD - 1); ii >= 0; ii--) {
      genetic_pool[ORGANISMS_PER_GEN * ii + i] = genetic_pool[i].reproduce(i);
    }
  }
  generation++;
	return best;
}

void train(int imax) {
  for (int i = 0; i < imax; i++) {
    simulate_generation();
  }
	const auto best = simulate_generation();
	std::cout << "\n Last generations' best was: " << best.x2 << "x^2 + " << best.x1 << "x + " << best.c << "\n";
}
	
} // namespace machineLearning

int main()
{
	machineLearning::train(10000);
	return 0;
}

