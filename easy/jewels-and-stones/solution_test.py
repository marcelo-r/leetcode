import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        test = {"J": "aA", "S": "aAAbbbb"}
        want = 3
        got = Solution().numJewelsInStones(**test)
        self.assertEqual(want, got)

    def test_2(self):
        test = {"J": "z", "S": "ZZ"}
        want = 0
        got = Solution().numJewelsInStones(**test)
        self.assertEqual(want, got)

