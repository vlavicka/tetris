import sys
import unittest
sys.path.append('..')

from tools import testcommon
from playground import *

# TODO: playground representation -> 2D array MxN with information about
#       empty and filled tiles
# TODO: insert current moving piece -> piece representation
# TODO: set speed of current moving piece
# TODO: rotate current piece -> returns False when piece cannot be moved
# TODO: move current piece left or right
# TODO: drop current piece
# TODO: dump playground on screen (colored) or into list of strings

empty_playground = """\
+----+
|    |
|    |
|    |
|    |
|    |
|    |
|    |
|    |
+----+"""



class TestPlayGroundModel(unittest.TestCase):
    def setUp(self):
        self.model = PlayGroundModel(4, 8)

    def test_create_playground(self):
        """ create playground """
        self.assertEqual(4, self.model.width)
        self.assertEqual(8, self.model.height)
        self.assertEqual(0, sum(self.model._area))

    def test_dump_playground(self):
        """ dump playground into string """
        self.assertEqual(empty_playground, self.model.dump_str())
        
    def test_set_tile(self):
        """ set tile to specific color """
        self.model.set_color(0, 0, 1)
        self.assertEqual(1, self.model.get_color(0, 0))
        
    def test_check_filled_lines(self):
        """ check for filled lines """
        self.model.set_color(2, 6, 1)
        for i in range(4):
            self.model.set_color(i, 7, 1)
        self.assertEqual([7], self.model.get_filled())

    def test_check_filled_lines_multi(self):
        """ check for filled lines """
        self.model.set_color(2, 6, 1)
        for i in range(4):
            self.model.set_color(i, 7, 1)
            self.model.set_color(i, 5, 1)
        self.assertEqual([5, 7], self.model.get_filled())


    # TEST: remove filled lines

    # TEST: dump colored playground onto screen

if __name__ == "__main__":
    testcommon.run_unit_tests(globals())

