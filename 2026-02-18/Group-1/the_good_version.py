from pathlib import Path
import sys
import random

def get_words_from_file(filename: str) -> list[str]:
    """Returns non-plural lowercase words in file"""
    lines = Path(filename).read_text().splitlines()
    return [
        line for line in lines 
        if line.islower() and not line.endswith("'s")
    ]

def game_loop(words: list[str]) -> None:
    """Play the dictionary game"""
    score = 0
    used = set()
    cpu_word = random.choice(words)
    print(f"CPU Word: {cpu_word}")

    while True:
        user_word = input("Your word: ")
        if not user_word or not user_word.startswith(cpu_word[-1]):
            print(f"You lose, invalid word, score: {score}")
            return
        
        used.add(user_word)
        valid_words = [
            w for w in words 
            if w.startswith(user_word[-1]) and w not in used
        ]

        if not valid_words:
            print("You win!")
            return

        cpu_word = random.choice(valid_words)
        print(f"CPU Word: {cpu_word}")
        used.add(cpu_word)


def main() -> None:
    if len(sys.argv) != 2:
        print("Please pass a file name as an argument")
        return
    
    try:
        words = get_words_from_file(sys.argv[1])
    except FileNotFoundError:
        print("File does not exist")
        return
    
    game_loop(words)
    


if __name__ == "__main__":
    main()
