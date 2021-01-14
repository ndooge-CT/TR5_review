import unittest
import robot
from world.text import world as world
from maze import obstacles as obstacles
from io import StringIO
from test_base import run_unittests
from test_base import captured_io


class MyTestCase(unittest.TestCase):
    def test_check_observations(self):
        return True


if __name__ == '__main__':
    unittest.main()
