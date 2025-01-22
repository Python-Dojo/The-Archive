"""
Helper for Wordle/Hardle: given the information you have so far, which words could be the answer?
"""

# 1 take user input eg. hello 00112 0=incorrect 1=correct letter +wrong location 2=correct
# 2 sanitise user input
# 3 loop - get suggestions, print suggestions, take another suggestion
# 4 when only 1 suggestion, break the loop

from enum import Enum

def _get_words():
    with open("words.txt", "r") as file:
        return file.read().split()

VALID_WORDLE_WORDS = _get_words()

class CharState(Enum):
    Incorrect = 0
    Wrong_Location = 1
    Correct = 2
    
class WordleGuess:

    word: str
    char_state: list[CharState]

    def __init__(self, guess_input):
        self.word = guess_input.split(" ")[0]
        self.char_state = [int(x) for x in guess_input.split(" ")[1]]
       

def validation_guess(input:str):
    """
    Guess should in format ABCDE 00000
    """
    split_input = input.split(" ")
    if (len(split_input) != 2):
        raise Exception('String was the wrong format, should be in "ABCDE 00000"')
    guess = split_input[0]
    correctness = split_input[1]
    if (len(guess) != 5):
        raise Exception("Bad input, guess length")
    if (len(correctness) != 5):
        raise Exception("Bad input, correctness length")
    if (not guess.isalpha() or not guess.isascii()):
        raise Exception(f'Bad guesss input: "{input}"')
    if (not correctness.isnumeric() or not correctness.isascii):
        raise Exception(f'Bad correctness "{input}"')
    return guess, correctness

def get_guess():
    _input = input("Please enter your guess: ")
    return validation_guess(_input)
# string toint python
def main():
    guesses = []
    while (True):
        try:
            guess = get_guess() # hello 00112
        except Exception as e:
            print(e)
            continue

        guesses += [WordleGuess(guess)]
        suggestions = get_suggestions(guesses)
        print(", ".join(suggestions))
        if (len(suggestions) == 1):
            break
    

def get_suggestions(guesses: list[WordleGuess]) -> list[str]:
    return ["wordl"]


def step(guess: str, response: list[int]) -> list[str]:
    ...



if __name__ == "__main__":
    main()