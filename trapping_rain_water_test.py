import unittest
from trapping_rain_water import *


class rainwaterTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        vals = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(self.solution.trap(vals), 6)


def main():
    unittest.main()


if __name__ == '__main__':
    main()


