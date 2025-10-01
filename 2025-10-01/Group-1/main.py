
# todo list app
import typing
import argparse
from argparse import ArgumentParser

import json

def load(filename: str):
    f = open(filename, "r")
    data = json.load(f)
    f.close()
    return data

def save(filename: str, data):
    f = open(filename, "w")
    json.dump(data, f)
    f.close()

# Wrap print
def print_to_screen(stringable:typing.Any):
    ...

def create_arg_parser():
    return argparse.ArgumentParser(prog="TODOList™", description="is a todo list")

def create_add_subcommand(sub_parsers):
    """
    Is responable for the usage:
        `todo.py add "a string"`  
    """
    (sub_parsers
        .add_parser("add",  help="add - add an item to the do do list")
        .add_argument("added_item", metavar="files", type=str, nargs=1)
    )

def create_done_subcommand(sub_parsers):
    """
    Is responable for usage:
        `todo.py done "key"`
    """
    (sub_parsers
        .add_parser("done", help="done - mark a todo list item as done ")
        .add_argument("item", metavar="files", type=str, nargs=1)
    )

def create_edit_subcommand(sub_parsers):
    """
    Is responable for usage:
        `todo.py edit delete "key"`
    &&  `todo.py edit rename "input" "end"`
    """
    parser = sub_parsers.add_parser("edit", help="edit - edit a current todo list item")    
    parser.add_argument("delete", type=str, nargs=1)
    parser.add_argument("rename", type=str, nargs=2)

def main():
    arg_parser = create_arg_parser()
    # sub_parsers = arg_parser
    sub_parsers = arg_parser.add_subparsers()
    create_done_subcommand(sub_parsers)
    create_add_subcommand(sub_parsers)
    create_edit_subcommand(sub_parsers)
    parsed = arg_parser.parse_args()
    
    data:dict[str, bool]
    try:
        data = load("todolist.json")
    except:
        data = {"nothing works": True}

    if parsed.added_item:
        data.update({ item : False for item in parsed.added_item })
    elif parsed.edit.rename:
        data.update(parsed.edit.rename[1], data[parsed.edit.rename[0]])
    elif parsed.edit.delete:
        data.pop(parsed.edit.delete)

    save("todolist.json", data)
    
if __name__ == "__main__":
    main()
else:
    exit("This file was imported, that is not expected usage")


# Usage:

# todo.py add "a string"
# todo.py done "key"
# todo.py edit delete "key"
# todo.py edit rename "input" "end"


