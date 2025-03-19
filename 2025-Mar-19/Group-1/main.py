
# Hello world

# Given a dictionary with uuids representing players as keys and float 0-10 || 11,
#  organise them into groups of around 5 where each group has one 11 and otherwise 
#  have similar values. Each group should be of similar size

UUID = int

# TODO 
# - take the dict and determin max number of groups
#  - a = number of 11s
#  - b = len(dict) // 3
#  - min(b, a) == max number of groups

MIN_SIZE_OF_GROUP = 3

def max_number_of_groups(data:dict) -> int:
    number_of_admins = 0
    for value in data.values():
        if value == 11:
            number_of_admins += 1
    if (number_of_admins <= 1):
        raise Exception("One or fewer admins present, refusing to group into teams")
    max_from_admins = number_of_admins;
    max_from_group_size = max(len(data) // MIN_SIZE_OF_GROUP, 1);

    return min(max_from_group_size, max_from_admins)

# - function for checking if confidence is a valid value
def assert_valid_confiedence_valid(data:dict) -> None:
    for value in data.values():
        if value == 11.0:
            continue
        if value < 0:
            raise Exception(f"Invalid confidence value: {value}, must be greater than 0")
        if value > 10:
            raise Exception(f"Value: {value} was greater than 10 but was not 11")

# - function 
Group = list[UUID]

def organise_admins(data:dict, number_of_groups:int) -> list[Group]:
    admins_organised = 0;
    result_groups: list[Group] = []
    for key, value in data.items():
        if value == 11:
            if admins_organised < number_of_groups:
                result_groups.append([key])
            else:
                index_with_fewest_admins = admins_organised % number_of_groups
                result_groups[index_with_fewest_admins].append(key)
            admins_organised +=1
        else:
            group_lens = [ len(x) for x in result_groups ]
            
    return result_groups

def sort_into

if __name__ == "__main__":
    ...