# Task

Build a system that can scan a project directory, find Python classes, and create a factory or registry that can instantiate those classes automatically.

This date folder contains three separate approaches from the 2023-11-15 Bristol Python Dojo session, all working toward the same broad goal: discovering classes in files or subdirectories and using that metadata to construct class instances or default factories.

## The shared problem

The core theme across the session was:

- walk through a directory tree
- inspect Python source files
- find `class` definitions using regex or string parsing
- record the class names and their file locations
- use that information to produce a factory with default objects or imports

This is a common pattern in frameworks and code generators, where the system learns about available classes dynamically instead of hardcoding each one manually.

## Group 1: directory scanning for class discovery

Directory: `Group-1`

File: `main.py`

This version is the most direct and exploratory implementation.

It uses `os.walk()` to traverse a subdirectory and inspect files for lines beginning with `class`:

```python
for root, dirs, files in os.walk(subdirectory):
    ...
```

The code includes a function named `check_for_class(file_path: str) -> list`, which reads each file line by line and returns any lines that start with `class`:

```python
if str(line).startswith("class"):
    content.append(line)
```

This is a rough implementation of class discovery but not yet a complete solution. It demonstrates the right idea: scan source files to find class declarations, then treat those as metadata that can be used later to generate factories or registries.

The code also contains commented-out regex and a placeholder `get_files_with_class(...)` function, showing the team was exploring a more formal class-detection approach before finishing the implementation.

## Group 2: prototype factory and dynamic import logic

Directory: `Group-2`

Files: `main.py`, `classes/ExampleClass.py`

This group tries to go beyond scanning and actually construct a factory-like object from discovered classes.

The script defines a `Factory` class with a `classes` dictionary, beginning with a simple example:

```python
self.classes = {
    "Book": Path("src/book.py"),
}
```

The intention is to map class names to file paths and then dynamically import them. The code tries to build an import path like this:

```python
path = ".".join(self.classes[class_name].as_posix().replace(".", "/").split("/")[:-1])
code = f"from {path} import {class_name}"
exec(code, globals())
```

This is an early step toward a runtime loader that could import a class from a Python module and inspect it.

It also imports `inspect` and attempts to read constructor signatures using `inspect.signature(...)`, which is a natural next step once a class has been imported. The idea is to build a default factory by understanding each class constructor and filling in values automatically.

This version is more ambitious but less complete. The file contains several experimental and invalid snippets, including stray text and malformed Python, so it reads more like a brainstorming prototype than a finished script.

## Group 3: regex-driven discovery and factory scaffolding

Directory: `Group-3`

File: `main.py`

This is the most structured and recognisably "solution-oriented" version of the group work.

It defines two key regex patterns:

```python
FIND_CLASSES_RE = r"^class ([\w_]+)"
FIND_INIT_RE = r"\W+def __init__\(self([^)]*)"
```

These are used to identify:

- class names in source files
- the constructor signature of those classes

The script then scans files in the current working directory and yields any classes it finds:

```python
def get_classes():
    for file_name in files_gen(os.getcwd()):
        with open(file_name, "r") as file:
            for line in file.readlines():
                match = re.match(FIND_CLASSES_RE, line)
                if match is not None:
                    yield file_name, match.group(1)
```

This is the clearest expression of the original task: find classes and maybe later instantiate them.

It also includes helper functions to:

- convert a class name to a plausible instance name
- import a class from a module
- produce a default object when a specific condition is met

The main function `main(idea: str)` is a placeholder for a factory-style dispatch system that might return different default objects based on a user idea or specification.

## Common ideas across the session

Across all three groups, the same broad concepts appear repeatedly:

- use regex or string matching to find `class` declarations
- scan directories recursively for files to inspect
- read constructor signatures to learn what arguments each class requires
- import the discovered class dynamically
- build a registry or factory with default instances

This is a strong example of a dojo session where the task is not solved in one clean, final implementation, but instead explored through multiple partially working prototypes.

## Why this is interesting

The code is a good illustration of the difficulty of writing a general-purpose class loader:

- not all Python projects use the same layout
- class definitions may be nested or indirect
- import paths can be complex
- constructors may require arguments that are hard to infer automatically
- dynamic execution with `exec` or `importlib` introduces risk and complexity

This means the session's work is valuable not because it produces a production-ready factory, but because it explores the design space and experiments with multiple practical strategies.

## Running the examples

Each group is a separate script. For example:

```bash
cd 2023-11-15/Group-1
python main.py
```

```bash
cd 2023-11-15/Group-2
python main.py
```

```bash
cd 2023-11-15/Group-3
python main.py
```

The scripts are intentionally rough and may not run cleanly as-is, but they are useful as historical examples of the problem-solving process.

## Summary

This folder represents one of the core dojo themes: writing code that can inspect and understand other code. The session produced three different attempts at the same challenge:

- Group 1: filesystem scanning and class detection
- Group 2: prototype factory and import logic
- Group 3: regex-based discovery with a more explicit class registry pattern

The result is not a finalised framework, but it is a valuable archive of working ideas and partial implementations.
