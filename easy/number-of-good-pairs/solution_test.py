import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1,2,3,1,1,3]
        want = 4
        got = Solution().numIdenticalPairs(nums)
        self.assertEquals(want, got)

    def test_2(self):
        nums = [1,1,1,1]
        want = 6
        got = Solution().numIdenticalPairs(nums)
        self.assertEquals(want, got)

    def test_3(self):
        nums = [1,2,3]
        want = 0
        got = Solution().numIdenticalPairs(nums)
        self.assertEquals(want, got)

