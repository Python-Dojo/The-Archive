import re
import itertools

def isOnlyABC(str:str) -> bool:
    for s in str:
        if(not["a", "b", "c"]):...
        
        
    return True

def is_string_cool(s:str) -> bool:
    """
    s only contains the letters 'a', 'b', and 'c'.
    s does not contain any of "aaa", "bbb", or "ccc" as a substring.
    s contains at most a occurrences of the letter 'a'.
    s contains at most b occurrences of the letter 'b'.
    s contains at most c occurrences of the letter 'c'.
    """
    return not re.findall(r"a{3,}|b{3,}|c{3,}", s)
    
def longest_diverse_string(a: int, b: int, c: int) -> str:
    """
    Returns any longest string with at most a 'a's b 'b's and c 'c's
    Cannot contain 'aaa' 'bbb' or 'ccc' anywhere in the string
    """
    characters = "a" * a + "b" * b + "c" * c

    perms = []
    for i in range(1, len(characters) + 1):
        perms.extend(itertools.permutations(characters, i))
    all_strings = ["".join(tup) for tup in perms]
    valid = [string for string in all_strings if is_string_cool(string)]

    return max(valid, key=lambda s: len(s), default="")

        
    




