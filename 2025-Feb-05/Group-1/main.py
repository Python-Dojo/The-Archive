
def create_line(column_names:list[str], fill_character:str = "*", spacings:list[int]|None = None):
    """
    columns_names: list[str] <- this signifies that column_names will be a list of strings
    spacings: list[int] | None <- this signifies that spacings should be either a list of integers, or None
    spacings: list[int] | None = None <- adding the = None means that spacings should default to being None if not passed in
    """
    # check the fill_character is exactly one character
    assert len(fill_character) == 1
    # Check the fill character is not white space
    assert fill_character.strip()
    # if we did not specify the spacings variable
    if spacings is None:
        # set spacing to something reasonable
        spacings = [7] * len(column_names)
    # Create the column name with some spacing before and after the word
    padded_columns = [ str(c).center(w) for c, w in zip(column_names, spacings) ]
    # Add a the fill character to the start and end of the line
    return f'{fill_character} {f" {fill_character} ".join(padded_columns)} {fill_character}'

def fill_line(length: int, fill_character:str = "*") -> str:
    """Return length copies of the provided fill character"""
    return fill_character * length

def get_headers_from_csv(file:str) -> list[str]:
    """open file and return a list of all the items in the fi"st row, "p"""
    # open the file
    with open(file, "r") as file :
        # get the first line
        first_line = file.readline()
        # strip the new line character from the string
        # split the remaining string into a list of strings on each ","
        # see `string.split` docs
        return first_line.strip("\n").split(",")

def main():
    column_names = get_headers_from_csv("ExampleFile.csv")
    header = create_line(column_names)
    spacings = [max(7, len(name)) for name in column_names]
    print(fill_line(len(header)))
    print(header)
    print(fill_line(len(header)))
    print(create_line([0.0, 0.1, .2, .6, .1], spacings=spacings))


if __name__ == "__main__":
    main()

    # Everything below here would usually go in a separate test_something.py file
    import unittest
    # 
    class test(unittest.TestCase):

        def test_default_fill(self):
            self.assertIn("*", fill_line(10))

        def test_non_default_fill(self):
            self.assertIn("i", fill_line(10, "i"))
        
        def test_not_in_custom(self):
            self.assertNotIn("*", fill_line(2, "i"))

        def test_default_header(self):
            self.assertIn("*", create_line([1]))

        def test_non_default_header(self):
            self.assertIn("i", create_line([3], "i"))
        
        def test_not_in_custom_header(self):
            self.assertNotIn("*", create_line([2], "i"))

        

    exit(unittest.main())

