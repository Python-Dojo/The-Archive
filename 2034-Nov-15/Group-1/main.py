# use regex to go through a file and or subdirectory,
# find all the classes in that subdirectory,
# then populate a factory with default initialisations
# of the results

import os

# get subdirectory
# make folders for testing -- manual job
# make classes for testing -- manual job
# write regex to check for classes
# get files classes are in
# import classes


def get_subdirectory() -> str:
  """ optionally get this from input or return a 
    constant item   
    """
  a = "name"
  print(a[1])

  return a

  ...


# finds if a class exists in a
# def has_class(file_data:str) -> bool:
#     """
#     Finds if a class is in the file_data and if so returns the name.
#     """
#     # ^ matches start of string. class matches class
#     regex_expression:str = r"^class";
#     matches = re.findall(regex_expression, file_data);
#     return bool(matches);


def get_files_with_class(subdirectory: str):
  """return a list of files that contain classes in them
    """
  for root, dirs, files in os.walk(subdirectory):
    ...


def check_for_class(file_path: str) -> list:
  content: list[str] = []
  with open(file_path, "r") as f:
    for line in f:
      if str(line).startswith("class"):
        content.append(line)

  return content
  
