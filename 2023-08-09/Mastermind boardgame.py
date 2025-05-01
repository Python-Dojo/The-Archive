import random

if __name__ != "__main__":
  print("running as module is not supported");
  exit(1);


FULL_LIST:str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

chosen_word:str|None = None;

# Create list of valid characters
def create_valid_charaters(number_of_characters:int) -> list[str]:
  return [*FULL_LIST][:number_of_characters];



# Pick random characters from list
def pick_random_char_from_list(char_list:list[str]) -> str:
    return char_list[random.randrange(0, len(char_list))];

# Get length of things to guess
def get_difficulty() -> int:
    min_difficulty:int = 1;
    max_difficulty:int = len(FULL_LIST);
    
    chosen_difficulty:int = 0;
    chosen_difficulty_unparsed:str = "";
    
    while True:
        chosen_difficulty_unparsed = input(f"Choose a difficulty from 1 to {max_difficulty}:\n")
        try:
            is_valid:bool = min_difficulty < int(chosen_difficulty_unparsed) < max_difficulty;
            if is_valid:
                break;
        finally:
          pass;
        print("Please choose a whole number from the given range.");
    chosen_difficulty = int(chosen_difficulty_unparsed);
    print(f"Chosen characters are {create_valid_charaters(chosen_difficulty)}")
    
    return chosen_difficulty;


# Get player guesses
def get_guess(length_of_guess:int) -> str:
  guess:str = input("Please guess a sequence of characters:\n");
  failed = True;
  invalid_characters:str = "-+~#!£$%^&*(){}[]";
  while (failed):
    failed = (len(guess) != length_of_guess);
    if failed:
      print(f"guesses must be {length_of_guess} characters long");
    else:
      for char in invalid_characters:
        if char in guess:
          print(f"character {char} was not a valid character")
          failed = True;
          break;
    if not failed:
      return guess;
    guess = input("Guess was not valid, please try again:\n");


# Score guess
def get_score(valid_guess:str, valid_target:str) -> int:
    black_pegs:int = 0
    white_pegs:int = 0

    guess_chars = [*valid_guess]
    target_chars = [*valid_target]
    
    # Get black pegs
    for i in range(len(target_chars)):
        if guess_chars[i] == target_chars[i]:
            black_pegs +=1
            target_chars[i] = "*"
            guess_chars[i] = "!"

    # Get white pegs
    for i in range(len(valid_target)):
        if guess_chars[i] in target_chars:
            white_pegs += 1
            target_chars[target_chars.index(guess_chars[i])] = "*"

    if black_pegs == 0 and white_pegs == 0:
        print("Try again.")
    else:
        print(f"{'⚫ '*black_pegs}{'⚪ '*white_pegs}")
    
    return black_pegs

# Get correct answer
def create_correct_answer(length:int) -> str:
  correct_answer:str = "";
  difficulty:int = get_difficulty();
  valid_characters:list[str] = create_valid_charaters(length);
  for i in range(length):
    chosen_char:str = pick_random_char_from_list(valid_characters);
    correct_answer = f"{correct_answer}{chosen_char}";
  return correct_answer;

# main
def main():
  score:int = 0;
  LENGTH_OF_ANSWER:int = 4
  correct_value = create_correct_answer(LENGTH_OF_ANSWER);
  rounds:int = 0;
  while (score != LENGTH_OF_ANSWER):
    guess:str = get_guess(LENGTH_OF_ANSWER);
    score = get_score(guess, correct_value);
    rounds += 1;
  print(f"Congrats you won in {rounds} rounds!")
  
main();
  
