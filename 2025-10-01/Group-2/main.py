"""Create a command line to-do app

https://docs.python.org/3/library/argparse.html

- add --list "popcorn" --description "check if there is any popcorn left" --date "2025-10-10"
- add --list "chores" --description "take out the bins"
- update --id 10 --description "take out the recyling"
- delete <id>
- show <list>

Example:
(freya@macos) ~ python3 main.py
>>> add "task name" --list "testing"
task created
>>> 
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
import argparse
from datetime import datetime
import shlex

def get_parser():
    parser = argparse.ArgumentParser(prog="todo")
    subparsers = parser.add_subparsers()

    add_subparser = subparsers.add_parser("add")
    add_subparser.add_argument("--list")
    add_subparser.add_argument("--description")
    add_subparser.add_argument("--date", default=None)

    show_subparser = subparsers.add_parser("show")
    show_subparser.add_argument("list")

    update_subparser = subparsers.add_parser("update")
    update_subparser.add_argument("id", type=int)
    update_subparser.add_argument("--list")
    update_subparser.add_argument("--description")
    update_subparser.add_argument("--date")

    delete_subparser = subparsers.add_parser("delete")
    delete_subparser.add_argument("id", type=int)

    return parser


@dataclass
class Todo:
    list_name: str
    description: str
    date: datetime | None = None

@dataclass
class TodoApp:
    todos: dict[int, Todo] = field(default_factory=lambda: {})
    id_counter: int = 0

    def add_todo(self, todo: Todo) -> int:
        self.id_counter += 1
        self.todos[self.id_counter] = todo
        return self.id_counter

    def update_todo(self, todo_id: int, todo: Todo) -> Todo:
        self.todos[todo_id] = todo
        return todo

    def delete_todo(self, todo_id: int) -> None:
        del self.todos[todo_id]

    def show_list(self, todo_list: str) -> None:
        """Display the todos for the requested list"""
        items_found = 0
        for idx, todo in self.todos.items():
            if not todo.list_name == todo_list:
                continue
            items_found += 1
            date_limit = f" - [{todo.date}]" if todo.date else ""
            print(f"- [{idx}]: {todo.description}{date_limit}")
        if not items_found:
            print(f"No list `{todo_list}` found")
        print()

    def serialise_to_json(self) -> str:
        return json.dumps([
            {
                "id": _id,
                "list_name": todo.list_name,
                "description": todo.description,
                "date": datetime.strftime(todo.date, format="%Y-%m-%d") if todo.date else None,
            } for _id, todo in self.todos.items()
        ], indent=4)
        
    @staticmethod
    def deserialise_from_json(j: str) -> TodoApp:
        raw_todos = json.loads(j)
        todos = { 
            e["id"]: Todo(
                list_name=e["list_name"],
                description=e["description"],
                date=datetime.strptime(e["date"], "%Y-%m-%d") if e["date"] else None,
            ) for e in raw_todos
        }

        max_id = max(todos, default=0)
        return TodoApp(
            todos=todos,
            id_counter=max_id,
        )

def main() -> None:
    parser = get_parser()

    with open("todos.json", encoding="utf-8") as f:
        data = f.read()

    app = TodoApp.deserialise_from_json(data)

    print("Welcome to the Todo App")
    print("use `(add|update) --list <todo_list> --description <what_to_do> --date <optional_completion_date>` to create or update a todo")
    print("use `delete --id <todo_id> to delete a todo")
    print("use `show <todo_list> to show all todos in a particular todo list")

    while True:
        response = input()

        if response == "exit":
            print("finished with todos")
            app_json = app.serialise_to_json()
            with open("todos.json", "w", encoding="utf-8") as f:
                f.write(app_json)
            return
            
        if response == "debug":
            print(app)
            continue

        subparser, *args = shlex.split(response)
        parsed = parser.parse_args([subparser, *args])

        if subparser in {"add", "update"}:
            description = parsed.description
            list_name = parsed.list
            raw_date = getattr(parsed, "date")
            completion_date = datetime.strptime(raw_date, "%Y-%m-%d") if raw_date else None
            todo = Todo(list_name=list_name, description=description, date=completion_date)

        if subparser == "add":
            todo_id = app.add_todo(todo)
            print(f"todo added: id = {todo_id}")
        if subparser == "delete":
            try:
                app.delete_todo(parsed.id)
                print(f"todo deleted: id = {parsed.id}")
            except KeyError:
                print(f"No todo found with id {parsed.id}")
        if subparser == "update":
            app.update_todo(parsed.id, todo)
            print(f"updated todo: id = {parsed.id}")
        if subparser == "show":
            app.show_list(parsed.list)


if __name__ == "__main__":
    main()
