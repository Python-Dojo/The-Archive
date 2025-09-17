
from dataclasses import dataclass
from main import DataBase, Clue, MockDatabase


class TestDatabase:
    def test_simple(database: DataBase):
        # Make some toy data
        dummy_clues: list[Clue] = [
            Clue(1, 1, "hello ?????", "world", False),
            Clue(1, 2, "life, the universe and everything", "fortytwo", True),
            Clue(1, 3, "not yes", "no", False),
            Clue(7, 12, "Find out", "discover", True),
        ]

        # Add to the database
        for dummy in dummy_clues:
            database.add_clue(dummy)

        # Load all cluses form the database
        retrieved_clues: list[Clue] = database.get_all_clues()

        # Loop over all clues, check the clues before and after are the same
        assert set(dummy_clues) == set(retrieved_clues), "Clues do not all match"

    def test_duplicates(database: DataBase):
        pass

def run_all_tests(database):
    TestDatabase.test_simple(database)
    # testDatabase.test_duplicates(mockDB)


if __name__ == "__main__":
    import tempfile
    with tempfile.NamedTemporaryFile() as f:
        mockDB: MockDatabase = DataBase(f.name)
        run_all_tests(mockDB)
        print("Success")
