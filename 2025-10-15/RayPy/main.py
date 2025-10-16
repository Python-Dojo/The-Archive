
# "Do what Rachel_Riley does on countdown"
# - target number (generate?)
# - Get prime factors of target
# - generate set of digits: inputset
# - see if prime factors are in inputset
#   + fudge input set to find said primes
# - solve (?)

from copy import deepcopy
import random
from typing import Literal, Sequence


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
    prime_factors = []
    if number == 1: return []
    for prime in _PRIMES[::-1]:
        if prime == number: return [prime]
        if prime > number: continue
        if number % prime == 0:
            # prime_factors.append(prime)
            return [prime] + get_prime_factors(number//prime)
    
    return prime_factors
    
def product[T](sequence:Sequence[T]) -> T:
    _iter = iter(sequence)
    total = next(_iter)
    for v in _iter:
        total *= v
    return total
        
def too_many_primes(target_primes:list[int], input_set:list[int]) -> Literal[False]|str:
    """
    times two primes togeather because #primes > #inputs
    call fudge with smaller targets  
    """
    # sanity check
    if product(target_primes) > product(input_set): return False
    # Shorten length of target (by creating a larger, non-prime) and recurse
    for i in range(len(target_primes)):
        new_target = deepcopy(target_primes)
        i_num = new_target.pop(i)
        for j in range(len(new_target)):
            if i == j: continue
            _new_target = deepcopy(new_target)
            # only ever mult (prime factors)
            new_item =  i_num * _new_target.pop(j)
            _new_target.append(new_item)
            if (result := fudge_to_find(_new_target, input_set)):
                assert result is not None
                return result 
    return False

def is_trivial(target_primes:list[int], input_set:list[int]) -> bool:
    _target_primes = deepcopy(target_primes)
    for input in input_set:
        if input not in _target_primes:
            return False
        _target_primes.remove(input)
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
    if not target_primes: raise ValueError("Cowardly refusing to find nothing")
    if not input_set: return False
    # if everything in target is in input set return target to string (no fuding required)
    if is_trivial(input_set, target_primes):
        return "*".join([str(i) for i in target_primes])

    if len(target_primes) >= len(input_set):
        return too_many_primes(target_primes, input_set)
    
    # if a target number 
    # have target number(s) and some input numbers - find combo of input numbers that makes the target nos
    
    # region: remove trival constructable values
    smaller_list = deepcopy(target_primes)
    bigger_list = deepcopy(input_set)

    i = 0
    trival = []
    while i < len(smaller_list):
        value = smaller_list[i]
        if smaller_list[i] in bigger_list:
            smaller_list.pop(i)
            bigger_list.remove(value)
            trival.append(value)
        else:
            i += 1        
    # print(f"{trival=}")
    if not smaller_list:
        # we are done
        return "*".join([str(t) for t in trival])
    if len(smaller_list) != len(target_primes) and bigger_list:
        # else problem set is reduced, something went well
        res = "*".join([str(t) for t in trival]) + "*"
        if len(smaller_list) == 1:
            single_find = find(smaller_list[0], bigger_list)
            if not single_find: return False
            return res + single_find
        
        single_find = find(product(smaller_list), bigger_list)
        if not single_find: return False
        res += single_find
        return res
    return False
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

def find(target:int, input_list:list[int]):
    if target in input_list: return f"{target}"
    # never going to work
    if 1 >= len(input_list): return False
    prime_factors = get_prime_factors(target)
    if not prime_factors: return False
    # print(f"prime factors of {target}, were {prime_factors}")
    # print(f"Attempting to create {target}->{prime_factors} with {input_list}")

    if (len(prime_factors) != 1) and (found := fudge_to_find(prime_factors, input_list)):
        print(f"Created factors of {target}: {prime_factors} with {input_list}: {found}")
        return found
    for input in input_list:
        new_target = target-input
        if new_target == 0: return f"{target}+{input}" # well that was lucky
        new_input_list = deepcopy(input_list)
        new_input_list.remove(input)
        if new_target < 0:
            if (target%input != 0): continue
            # try division for new target
            f = find(target//input, new_input_list)
            if f:
                print(f"Created factors of {target}: {prime_factors} with {input_list}: ({input}+{f})")
                return f"({input}*{f})"
        else:
            f = find(new_target, new_input_list)
            if f:
                print(f"Created factors of {target}: {prime_factors} with {input_list}: ({input}+{f})")
                return f"({input}+{f})"
    return False
        

def test_find_happy(number:int, inputs:list[int]):
    print("attemping ", number)
    assert number == eval(find(number, inputs))

def test_find_sad(number:int, inputs:list[int]):
    if res := find(number, inputs): print(res+(" =" if eval(res) == number else " !") + f"={number}")

def main():
    input_list = generate_set_of_digits(1)
    target_number = generate_target_number()
    find(target_number, input_list)

if __name__ == "__main__":
    main()

    # Testing
    def working():
        test_find_happy(174, [25, 10, 6, 4, 2, 3])
        print()
        test_find_happy(174, [25, 2, 2, 5, 2, 3])
        print()
        test_find_happy(172, [25, 2, 7, 5, 2, 3])
        test_find_happy(173, [25, 2, 2, 5, 2, 3])

    def broke():
        # print("impossible with current method")
        test_find_sad(6, [5,7])
        test_find_sad(18, [7,5,3])
        test_find_sad(172, [25, 2, 2, 5, 2, 3])
    
    print("BROKE\n")
    broke()

    print("\nWorks\n")
    working()
    print()
