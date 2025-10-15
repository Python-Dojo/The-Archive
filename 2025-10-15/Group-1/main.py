
# "Do what rachel riley does on countdown"
# - target number (generate?)
# - Get prime factors of target
# - generate set of digits: inputset
# - see if prime factors are in inputset
#   + fudge input set to find said primes
# - solve (?)

import random
from typing import Any, Literal

_PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,
127,131,137,139,149,151,157,163,167,173,
179,181,191,193,197,199,211,223,227,229,
233,239,241,251,257,263,269,271,277,281,
283,293,307,311,313,317,331,337,347,349,
353,359,367,373,379,383,389,397,401,409,
419,421,431,433,439,443,449,457,461,463,
467,479,487,491,499,503
]
def get_prime_factors(number:int) -> list[int]:
    print(f"{number=}")
    prime_factors = []
    if number == 1: return []
    for prime in _PRIMES[::-1]:
        if number % prime == 0:
            prime_factors.append(prime)
            return prime_factors + get_prime_factors(number/prime)
    
    return prime_factors
    
    
def too_many_primes(target_primes:list[int], input_set:list[int]) -> Literal[False]|str:
    """
    times two primes togeather because #primes > #inputs
    call fudge with smaller targets  
    """
    # Shorten length of target and recurse
    for i in range(len(target_primes)):
        new_target = target_primes
        i_num = new_target.pop(i)
        for j in range(len(new_target)):
            if i == j: continue 
            # only ever mult (prime factors)
            new_item =  i_num * new_target.pop(j)
            new_target = new_target.append(new_item)
            if (result := fudge_to_find(new_target, input_set)):
                return result 

def is_trivial(target_primes:list[int], input_set:list[int]) -> bool:
    for input in input_set:
        if input not in target_primes:
            return False
    return True

def return_smaller_list(a:list[int], b:list[int]) -> tuple[list[int], list[int]]:
    if len(a) < len(b):
        return (a, b)
    return (b, a)       

def fudge_to_find(target_primes:list[int], input_set:list[int]) -> Literal[False]|str:
    """
    fudge (e.g. (100 x 2) -1) them
    return remaining numbers
    retrun 
    """
    # if everything in target is in input set return target to string (no fuding required)
    if is_trivial(input_set, target_primes):
        # print(type(target_primes))
        return ",".join(target_primes)

    if len(target_primes) >= len(input_set):
        return too_many_primes(target_primes, input_set)
    
    used = []
    # if a target number 
    # have target number(s) and some input numbers - find combo of input numbers that makes the target nos
    
    smaller_list, bigger_list = return_smaller_list(input_set, target_primes)
    new_smaller = [i for i in smaller_list if i not in bigger_list]
    new_bigger = [i for i in smaller_list if i not in bigger_list]
    i 
    while :
        value = smaller_list[i]
        if smaller_list[i] in bigger_list:
            smaller_list.pop(i)
            bigger_list.pop(bigger_list.index(i))
                
        

    # just pick out the intersection
    
    for inp_idx, input_no in enumerate(input_set):
        if input_no in target_primes:
            target_primes.remove(input_no) # check remove uses val not idx
            input_set.pop(inp_idx)          
            used.append(input_no)
    if not target_primes:
        # got them all wooo
        return '*'.join(used)
    
    # now have the dregs - what to do
    # try pairs to get some action
    for inp_idx1, input_no1 in enumerate(input_set):
        for inp_idx2, input_no2 in enumerate(input_set):
            if inp_idx1 == inp_idx2:
                continue
            for op in [
                lambda x,y: x + y,
                lambda x,y: abs(x-y),
                lambda x,y: x / y if x%y == 0 else None,
                lambda x,y: y/x if y%x == 0 else None,
                lambda x,y: x * y,
            ]:
                value = op(input_no1, input_no2)
                if value is None:
                    continue
                
                
                

def generate_set_of_digits(number_of_large:int) -> list[int]:
    """
    generates a fixed amount of digits 
    if number_of_large > 4: raise 
    """ 
    if number_of_large > 4:
        raise ValueError("Number of large numbers must be 4 or fewer")

    large_nums = random.sample([25, 50, 75, 100], number_of_large)

    number_of_small = 6 - number_of_large
    small_nums_list = 2 * list(range(1, 11))
    small_nums = random.sample(small_nums_list, number_of_small)
    
    return large_nums + small_nums
    

def generate_target_number() -> int:
    """ generates a number between 100 - 999 """
    return int((random.random() * 899) + 100) 


if __name__ == "__main__":
    print(
        
    f"""
    {get_prime_factors(12)=}
    {get_prime_factors(6)=}
    {get_prime_factors(2)=}
    {get_prime_factors(2)=}
    """
    )
    # input_set = generate_set_of_digits(1)
    # target_number = generate_target_number()
    # print(input_set)
    # print(target_number)
    # prime_factors = get_prime_factors(target_number)
    # print(f"prime factors of {target_number}, were {prime_factors}")
    # found = fudge_to_find(prime_factors, input_set)
    # if found:
    #     print(found)
    #     print("sucess")
    #     exit(0) # success
    # print("failed")