from unittest import TestCase
from solution import Solution


class SolutionTest(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_base(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = self.sol.twoSum(nums, target)
        self.assertEqual(expected, result)

    def test_neg_1(self):
        nums = [-3, 4, 3, 90]
        target = 0
        expected = [0, 2]
        result = self.sol.twoSum(nums, target)
        self.assertEqual(expected, result)

    def test_neg_2(self):
        nums = [-3, 4, -3, 90]
        target = -6
        expected = [0, 2]
        result = self.sol.twoSum(nums, target)
        self.assertEqual(expected, result)

    def test_neg_3(self):
        nums = [-3, -3]
        target = -6
        expected = [0, 1]
        result = self.sol.twoSum(nums, target)
        self.assertEqual(expected, result)

    def test_3_3(self):
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        result = self.sol.twoSum(nums, target)
        self.assertEqual(expected, result)
