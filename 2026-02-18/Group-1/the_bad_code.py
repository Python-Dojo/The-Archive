"""
https://en.wikipedia.org/wiki/Word_chain
"""

import random
import sys

# from pathlib import Path


# class Example:

#     def __init__(self) -> None:
#         self.__thing = 1

# print(Example()._Example__thing)


# Why do we need a class for this
class Dictionary(BaseClass):

    # separate method to read a file and get words from it - not part of init
    def __init__(self, filename: str) -> None:
        words = []
        # should not open a file like this - no context manager & not closed properly
        f = open(filename)
        # better alternatives
        # with open(filename, encoding=<something>) as f:
        # Path(filename).read_text().splitlines()

        # alternative for this might be
        # lines = Path(filename).read_text().splitlines()
        # words = [line for line in lines if not line.endswith("'s") and line.islower()]
        for line in f.read().split("\n"):
            if line and not line.endswith("'s") and line.islower():
                words.append(line)
        random.shuffle(words)
        self.words = words

    def get(self, last: str):
        """
        Horrible way of getting a word that starts with the last character of last
        It removes the word from the list of available words at the same time.
        """
        for word in self.words:
            if not last or word[0] == last[len(last) - 1]:
                self.remove(word)
                return word
        return None

    def remove(self, word: str) -> None:
        self.words.remove(word)


if __name__ == "__main__":
    d = Dictionary(sys.argv[1])
    print(d.__Dictionary_words)
    score = 0
    last = None
    while True:
        last = d.get(last)
        print("%", last)
        word = input("> ")
        if word and word not in d.words:
            print("wrong\nscore:", score)
            break
        else:
            score += 1
            d.remove(word)
            last = word
