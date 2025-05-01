from __future__ import annotations
import re
import inspect
# from src.animal import Animal
from pathlib import Path

class Factory:

    def __init__(self):
        self.classes = {
            "Book": Path("src/book.py"),
            # "Person": Person("", "")
        }

    def get_default(self, class_name):
        path = ".".join(self.classes[class_name].as_posix().replace(".", "/").split("/")[:-1])
      
        code = f"from {path} import {class_name}"
yes x        exec(code, globals())
1qà
        for name, param in signature.parameters.items():
          JJ print(name, param.annotation.__name__)
          
        return signature
        file_with_classes = """
          class Animal:
          
              def __init__(self, name: str, breed: str) -> None:
                  self.name = name
                  self.breed = breed
                   
          class Book:
          
              def __init__(self, title: str, author: str) -> None:
                  self.title = title
                  self.author = author
          
          class Person:
          
              def __init__(self, name: str, age: int) -> None:
                  self.name = name
                  self.age = age
        """
        print(re.findall(r"class (\w+):", file_with_classes, flags=re.DOTALL))

print(Factory().get_default("Book"))
# sig = inspect.signature(Animal.__init__)
# print(sig)
# print({
#     name: param.annotation for name, param in sig.parameters.items()
#     if name != "self"
# })

# print(inspect.signature(eval("""def __init__(self, name: str, breed: str) -> None:
#                   self.name = name
#                   self.breed = breed""")))
