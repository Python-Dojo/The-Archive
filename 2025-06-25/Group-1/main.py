
# ASCII art file viewer
# TODO:
#  - Displaying some ascii art (print)
#       - for a folder
#       - for a file
#  - Retive current dir structure
#  - what order to print
#     - alphabetical
#     - last edited
#
#
#  Backlog
#       - group by file extenstion if extenstion occurences > 10 
#       - symlink
#       - tree
# 
# Example file
# /-----
# |     |
# | .py |
# |_____|
# 

import os

def get_cwd() -> str:
    """
    Returns the folder the user is currently in
    """
    return os.getcwd()

def get_data_from_dir(directory: str) -> str:
    return os.listdir(directory)

def is_symlink(file:str) -> bool:
    return os.path.islink(file)

def get_last_bit_of_path(any_path:str) -> str:
    return any_path.split("/")[-1]

def get_symlink_art(file:str) -> str:
    link_target = os.readlink(file)
    if link_target.find("/") != -1:
        link_target = "?/" + get_last_bit_of_path(link_target)
    return file.split("/")[-1] + " -> " + link_target + " 🔗"

def is_file(file:str) -> bool:
    return os.path.isfile(file)

def get_file_art(file:str) -> str:
    return f"{get_last_bit_of_path(file)} 📝"

def is_folder(any_path:str) -> bool:
    return os.path.isdir(any_path)

def get_folder_art(folder:str) -> str:
    return f"{get_last_bit_of_path(folder)} 📁"

def main() -> None:
    cwd = get_cwd()
    files = get_data_from_dir(cwd)
    for file in files:
        full_file_path = cwd + "/" + file
        if is_symlink(full_file_path):
            print(get_symlink_art(full_file_path))
        elif is_folder(full_file_path):
            print(get_folder_art(full_file_path))
        elif is_file(full_file_path):
            print(get_file_art(full_file_path))

if __name__ == "__main__":
    main()


