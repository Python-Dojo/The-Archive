# regex -- finds things in other things
# a regonsizes one item
# b regonsizes another item
# a | b returns true if a or b are recognised
# a* returns true if 0 or more "a"s are present
#

from collections.abc import Callable


# TODO
# Or operator
def or_operator(items_to_search: list, items_to_match:list) -> bool:
  # this returns true if any item in list is item_to_match
  # return any(item == item_to_match for item in items_to_search)
  # We want if the first item is any of items_to_match
  return any(items_to_search[0] == item for item in items_to_match)
  

# + operator
def plus_operator(items_to_search: list, item_to_match) -> bool | int:
  if len(items_to_search) == 0:
    return False
  if items_to_search[0] != item_to_match:
    return False
  i: int = 0
  for item in items_to_search[1:]:
    if item == item_to_match:
      i += 1
    else:
      return i
  return True


# any number of operator (empty list return true, else run + )
def any_number_of(items_to_search, item_to_match) -> bool | int:
  if len(items_to_search) == 0:
    return True
  return plus_operator(items_to_search, item_to_match)


# fixed number operator ( a{2} is two "a"s )
def n_number_of(items_to_search: list, item_to_match,
                number_of_matches: int) -> bool:
  if number_of_matches == 0:
    raise ValueError("Cannot match that zero items are the same")
  return all(item_to_match == item
             for item in items_to_search[:number_of_matches])


class PrimitiveIndexError(Exception):
  """Index of the primitive is not in [a-z][A-Z]"""


# a-z to index in second list
def get_index_from_string(index_str: str) -> int:
  index: int = ord(index_str)
  if index >= ord("a"):
    index -= ord("a")
    return index
  elif index >= ord("A"):
    index += 24
    index -= ord("A")
    return index
  raise PrimitiveIndexError("Outside of a-z A-Z range")


def get_number_from_brackets(input: str) -> int:
  start = input.find("{")
  end = input.find("}")
  number = input[start + 1:end]
  return int(number)


class UnknownOperatorError(Exception):
  """Operator not recognised"""


# matcher function, takes a list of items, some matching params and objects to match, returns a bool
def matcher(the_input: list, pattern: str, objects_to_match: list) -> bool:
  # hashmap/dict from operator string to function. ie vnjfrd = { "*" : any_number_of }
  OPERATOR_MAP: dict[str, Callable] = {
      "*": any_number_of,
      "+": plus_operator,
      "|": or_operator,
      "{": n_number_of
  }
  NON_ENDING_OPERATORS: list[str] = ["|"]

  match_indexes: list[int] = []
  search_index: int = 0
  operator = None
  should_do_func: bool = False
  in_or:bool = False
  pattern_index:int = 0
  for char in pattern:
    # if character is an operator, save it for when we do the matching
    operator = OPERATOR_MAP.get(char, None)
    print(operator)
    if operator is None:
      # if the character is not an operator it is an index
      match_indexes.append(get_index_from_string(char))
    else:
      # is operator
      if char not in NON_ENDING_OPERATORS:
        should_do_func = True
    if should_do_func:
      if operator is None:
        raise UnknownOperatorError(f"Don't what the operator is {char} ")
      if char == "{":
        number_of_matches:int = get_number_from_brackets(pattern[pattern_index:])
        a = n_number_of(the_input[search_index:], objects_to_match[match_indexes[0]], number_of_matches)
        # set flag to continue next two chars
      elif in_or:
        temp_obj_holder = []
        for i in match_indexes:
          temp_obj_holder.append(objects_to_match[i])
        a = or_operator(the_input[search_index:], temp_obj_holder)
      else :
        a = operator(the_input[search_index:], objects_to_match[match_indexes[0]])
      
      # if type(a) == bool:
      #   if a is False:
      #     return False
      if a is False:
        return False
      elif type(a) == int:
        search_index += a
  return True


# def

list_of_anything = []
a_obj = None
b_obj = 1
matcher(list_of_anything, "a*", [a_obj, b_obj])
