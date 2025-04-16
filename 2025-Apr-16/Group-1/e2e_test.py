
import unittest
from unittest import TestCase 

from grid import Grid

class EndToEndTest(TestCase):

    def test_empty(self):
        """
        Tests everything works
        """
        test_grid = Grid()
        self.assertEqual( test_grid.count_neighbours(0,0), 0)
        for row in test_grid.get_grid():
            for element in row:
                self.assertEqual(element, False)

    def test_

if __name__ == "__main__":
    unittest.main()