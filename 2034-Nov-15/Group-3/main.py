# use regex to go through a file and or subdirectory, find all the classes in that subdirectory, then populate a factory with default initialisations of the results.

# Read the file / subdirectory
# Make regex to read classes from a file
# Import classes
# Populate factory function with default initialisations

import re
import os
import importlib
from typing import List, Any

# madness: https://regex101.com/r/hoOWXV/1
FIND_CLASSES_RE = r"^class ([\w_]+)"
FIND_INIT_RE = r"\W+def __init__\(self([^)]*)"


def files_gen(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) and ".py" in file:
            yield file


def get_classes():
    for file_name in files_gen(os.getcwd()):
        with open(file_name, "r") as file:
            for line in file.readlines():
                match = re.match(FIND_CLASSES_RE, line)
                if match is not None:
                    yield file_name, match.group(1)
                    


def class_name_to_instance_name(classname: str) -> str:
    """turn classname into instance name"""
    instance_name = classname[0].lower()
    for char in classname[1:]:
        instance_name += ('_' + char.lower() if char.isupper() else char)
    return instance_name


def get_arguments(arg_list: str) -> None:
    args_with_defaults = arg_list.split(",")


def instantiate(file, class_name):
    module = importlib.import_module(file[:-3])
    return getattr(module, class_name)


def main(idea: str) -> Any:
    """main proc"""
    for filename, cls in get_classes():
        print(f"{filename}; {cls}")
        if idea == "hungry" and cls == "Cookie":
            return instantiate(filename, cls)
    

if __name__ == "__main__":
    user_idea = "hungry"
    test_instance = main(user_idea)
    print(str(test_instance))
