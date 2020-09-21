import unittest
from pascal import Solution

solution = Solution()


class TestSolution(unittest.TestCase):
    def test_1(self):
        test = 1
        want = [[1]]
        got = solution.generate(test)
        self.assertListEqual(want, got)

    def test_2(self):
        test = 2
        want = [[1], [1, 1]]
        got = solution.generate(test)
        self.assertListEqual(want, got)

    def test_3(self):
        test = 3
        want = [[1], [1, 1], [1, 2, 1]]
        got = solution.generate(test)
        self.assertListEqual(want, got)

    def test_5(self):
        test = 5
        want = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        got = solution.generate(test)
        self.assertListEqual(want, got)

    def test_8(self):
        test = 8
        want = [
                [1], 
                [1, 1], 
                [1, 2, 1], 
                [1, 3, 3, 1], 
                [1, 4, 6, 4, 1],
                [1, 5, 10, 10, 5, 1],
                [1, 6, 15, 20, 15, 6, 1],
                [1, 7, 21, 35, 35, 21, 7, 1]]
        got = solution.generate(test)
        self.assertListEqual(want, got)
