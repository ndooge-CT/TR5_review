from maze import obstacles as obstacles
import unittest
import robot


class MyTestCase(unittest.TestCase):

    def test_generate_obstacles(self):
        obstacles_ls = obstacles.generate_obstacles()
        self.assertTrue(0 <= len(obstacles_ls) <= 10)
        for item in obstacles_ls:
            self.assertTrue(-100 <= item[0] <= 100)
            self.assertTrue(-200 <= item[1] <= 200)
    
    def test_is_position_blocked(self):
        test_obs = (50, -100)
        obstacles.obstacles_ls.clear()
        obstacles.obstacles_ls.append(test_obs)
        

        self.assertEqual(True, obstacles.is_position_blocked(52, -97))
        self.assertEqual(False, obstacles.is_position_blocked(100, 50))

    def test_is_path_blocked(self):
        obs = (5,10)
        obstacles.obstacles_ls.clear()
        obstacles.obstacles_ls.append(obs)

        self.assertEqual(False, obstacles.is_path_blocked(0,0,6,0))
        self.assertEqual(True, obstacles.is_path_blocked(6,0,6,10))

if __name__ == '__main__':
    unittest.main()
