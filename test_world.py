import sys
import robot
import unittest
from world.text import world as world
from test_base import captured_io
from test_base import run_unittests
from io import StringIO
from maze import obstacles as obstacles
sys.path.append('/homes/ndooge/problems/submission_002-robot-4/world/')


class MyTestCase(unittest.TestCase):
    def test_is_position_allowed(self):
        self.assertEqual(True, world.is_position_allowed(95,100))
        self.assertEqual(False, world.is_position_allowed(101,201))
    
    def test_update_position_1(self):
        world.position_x = 0
        world.position_y = 0
        world.current_direction_index = 0

        self.assertEqual(True,world.update_position(100))
    def test_update_position_2(self):
        world.position_x = 0
        world.position_y = 0
        world.current_direction_index = 1

        self.assertEqual('boundary',world.update_position(101))
        


if __name__ == '__main__':
    unittest.main()
