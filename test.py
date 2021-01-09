import unittest

from main import load_to_array


class TestLoad(unittest.TestCase):

    def test_to_load(self):
        grid = load_to_array('testcase.csv')
        print(grid)
        self.assertEqual(grid, [['x', 'o', 'x'], ['x', 'y', 'x']])


if __name__ == '__main__':
    unittest.main()