import sys
import unittest
sys.path.append('..')

from tools import testcommon
import playground

# TODO: playground representation -> 2D array MxN with information about
#       empty and filled tiles
# TODO: insert current moving piece -> piece representation
# TODO: set speed of current moving piece
# TODO: rotate current piece -> returns False when piece cannot be moved
# TODO: move current piece left or right
# TODO: drop current piece
# TODO: dump playground on screen (colored) or into list of strings


class TestPlayGroundModel(unittest.TestCase):
    def test_create_playground(self):
        """ create playground """
        pass

        
    # TEST: dump playground into string
    # TEST: set tile to specific color
    # TEST: dump colored playground onto screen


    # TEST: check for filled lines
    # TEST: remove filled lines

if __name__ == "__main__":
    testcommon.run_unit_tests(globals())

