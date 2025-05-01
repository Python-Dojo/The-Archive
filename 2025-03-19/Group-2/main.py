"""
Task
Given a dictionary with uuid -> float 0-10 or a value of 11 as values (representing python experience)
Create groups of about the same size (5ish) with one 11 in each group
Groups should be of approximately the same skill

Example input:  
{
    "uuida": 11,
    "uuidb": 0.5,
    "uuidc": 8,
    "uuidd": 7.59,
    "uuide": 11,
    "uuidf": 8.1,
    "uuidg": 6.1,
    "uuidh": 4.8
}

Example output:
{
    "Group1": {
        "sum": 27.19,
        "uuids": ["uuida", "uuidb", "uuidf", "uuidd"],
    }
    "Group2": {
        "sum": 29.9,
        "uuids": ["uuide", "uuidg", "uuidh", "uuidc"],
    }
}

At least one admin per group
If not enough admins then promote the highest number
Minimum size of 3
Maximum size of 6

"""
import random
import uuid
import math
import json

MIN_SIZE = 3
MAX_SIZE = 6

EXAMPLE = {
    '286f1ec2d9aa41949b50aa34ef91f7b2': 11, 
    '97c8a84152a945f9bb1353304da820c9': 11, 
    '79fc4f1c583a4c319655cac43d0382cf': 0.4, 
    '09896255b178443bba46f315d39d3125': 1.0, 
    'b0cb27b234a34379a52352790ce588a4': 2.7, 
    'f4e3877ffb494eaa9794e20f41de2218': 1.4, 
    '8fe6c63c64b741af91de6b395b7bf9c2': 5.1,
    'af59e87246154ff6ba6bf054f54995ef': 4.7, 
    '5fd32b267ba644eb922116f33a62f253': 6.4, 
    'b4a00e5fd9904e1588afa5fa141730c5': 4.6, 
    '658887394cca4de89017e72f93463a3a': 7.9, 
    '99cc03281f1442f2bf50526a7e6f4d59': 5.4
}

def example_generator(admin_count: int, attendee_count: int) -> dict[str, float]:
    """Generate a dictionary with some number of admins & attendees for testing"""
    admins = {
        str(uuid.uuid4().hex): 11
        for _ in range(admin_count)
    }
    attendees = {
        str(uuid.uuid4().hex): random.randint(0, 100) * 1.0 / 10
        for _ in range(attendee_count)
    }
    return {**admins, **attendees}

def calculate_group_count(input_dict: dict) -> int:
    """How many groups should there be"""
    total_people = len(input_dict)
    if total_people <= 5:
        return 1
    count = 2
    while math.ceil(total_people / count) > MAX_SIZE:
        count += 1
    return count


def pretty_print(data: dict) -> None:
    print(json.dumps(data, indent=4))

def sort_by_value(data: dict) -> dict:
    """Sort the data by its values where the highest value items go first"""
    return {
        key: value for key, value in sorted(data.items(), key=lambda pair: pair[1], reverse=True)
    }

def sort_into_buckets(input_dict):
    groups = calculate_group_count(input_dict)
    sorted_dict = sort_by_value(input_dict)

    bucket_sum = [0 for _ in range(groups)]
    buckets = [[] for _ in range(groups)]

    for key, value in sorted_dict.items():
        minimum_value = min(bucket_sum)
        location = bucket_sum.index(minimum_value)
        bucket_sum[location] += value
        buckets[location].append(key)

    pretty_print(bucket_sum)
    pretty_print(buckets)
    return bucket_sum, buckets

pretty_print(sort_by_value(input_dict := example_generator(2, 14)))
sort_into_buckets(input_dict)
