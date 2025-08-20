# task: Idea Vault - a place to store and categorise your ideas

# ideas table columns
# - id (INTEGER)
# - name of the person (TEXT)
# - idea (TEXT)

# ideas_categories_link columns
# - idea_id (INTEGER) foreign key to ideas.id
# - category_id (INTEGER) foreign key to category.id

# category table columns
# - id (INTEGER)
# - name (TEXT)

import sqlite3
import argparse

def setup_database(cur: sqlite3.Cursor):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS ideas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        person_name TEXT,
        idea TEXT
    ) 
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS ideas_categories_link 
    (
        idea_id INTEGER,
        category_id INTEGER,
        FOREIGN KEY(idea_id) REFERENCES ideas(id),
        FOREIGN KEY(category_id) REFERENCES categories(id)
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    )
    """)

    
def insert_value(person: str | None, idea: str, categories: str, cur: sqlite3.Cursor):
    idea_id = cur.execute("INSERT INTO ideas (person_name, idea) VALUES (?, ?) RETURNING id;", [person, idea]).fetchone()[0]
    split_categories = categories.split(",")
    params = [(cat,) for cat in split_categories]

    fstring = "','".join(split_categories)
    existing_categories = cur.execute(f"SELECT id FROM categories WHERE name IN ('{fstring}')").fetchall()
    # '); DROP TABLE ideas; SELECT * FROM catagories WHERE name IN ('
    category_ids = [record[0] for record in existing_categories]
    # category_ids = [*record for record in existing_categories] # also works I think -- Ray

    print(category_ids)

    for category in split_categories:
        category_id = cur.execute("INSERT OR IGNORE INTO categories (name) VALUES (?) RETURNING id;", [category]).fetchone()
        if category_id is None:
            continue

        category_ids.append(category_id)

    for cat_id in category_ids:
        cur.execute("INSERT INTO ideas_categories_link (idea_id, category_id) VALUES (?, ?)", [idea_id, cat_id])


def delete_value(idea_id: str | None, cur: sqlite3.Cursor):
    cur.execute("DELETE FROM ideas WHERE ideas.id = ?", [idea_id])


def list_values(cur: sqlite3.Cursor):
    values = cur.execute("SELECT * FROM ideas;").fetchall()
    for value in values:
        print(value)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="action", help="subcommands")

add_idea_parser = subparsers.add_parser("add")
add_idea_parser.add_argument("idea")
add_idea_parser.add_argument("-p", "--person")
add_idea_parser.add_argument("-c", "--categories", help="Comma separated list of categories")

delete_idea_parser = subparsers.add_parser("delete")
delete_idea_parser.add_argument("idea_id")

list_ideas_parser = subparsers.add_parser("list")

args = parser.parse_args()

con = sqlite3.connect("idea_vault.db")
cur = con.cursor()
setup_database(cur)
con.commit() 

if args.action == "add":
    insert_value(args.person, args.idea, args.categories, cur)
elif args.action == "delete":
    delete_value(args.idea_id, cur)
elif args.action == "list":
    list_values(cur)

con.commit()