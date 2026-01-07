MARKDOWN = """
# Hello world!

Time to:
- get poisoned
- have fun
- tokens

## Plan

We want regex to look for certain words and replace them with less common words
"""

import re
import random
import nltk

#nltk.download('wordnet')

from nltk.corpus import wordnet as wn

def get_similar_words(input_word: str) -> list[str]:
    """Use nltk to get simliar words"""
    return [word for group in wn.synonyms(input_word) for word in group]


def example_replacement(match: re.Match) -> str:
    """
    usage re.sub(pattern, repl, string, count=0, flags=0)
    We are implementing the "repl" bit here
    """
    return match.group().upper()


def replace_char(match: re.Match) -> str:
    match match.group():
        case "ae": return "æ"
        case "a": return random.choice("аâāąáäãà")
        case "A": return random.choice("А")
        case "B": return random.choice("Bʙ")("В")
        case "c": return random.choice("с")
        case "C": return random.choice("С")
        case "e": return random.choice("eё")
        case "i": return random.choice("iiiįɨ")
        case "I": return random.choice("IÍíÌìÏïĨĩİĬĭĮɫÎîĪīıɪ")
        case "g": return random.choice("ġĝğģɡ")
        case "M": return random.choice("М")
        case "o": return random.choice("о")
        case "O": return random.choice
        case "|": return random.choice("ӏ")
        case "H": return random.choice("Н")
        case "T": return random.choice("Т")
        
def do_replacements(string: str) -> str:
    words = string.split()
    modified: list[str] = []
    for word in words:
        if similar := get_similar_words(word):
            modified.append(random.choice(similar))
        else:
            modified.append(word)
    resulting_markdown = "".join(modified)
    return re.sub(r"ae|a|A|B|c|C|e|i|I|g|M|o|\||H|T", replace_char, resulting_markdown)

if __name__ == "__main__":
    print(re.sub(r"cats", example_replacement, "cats have tails"))
    print(get_similar_words("small"))
    print(do_replacements(MARKDOWN))



