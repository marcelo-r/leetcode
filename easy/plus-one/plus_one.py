import unittest
import pdb

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        buffer = 1
        i = len(digits) - 1
        while buffer > 0:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                buffer = 0
                break
            i -= 1
            if i < 0 and buffer > 0:
                digits = [1] + digits
                buffer = 0
        return digits


class TestSolution(unittest.TestCase):
    def test_plus_0(self):
        digits = [0]
        got = Solution().plusOne(digits)
        want = [1]
        self.assertEqual(want, got)

    def test_plus_single(self):
        digits = [1]
        got = Solution().plusOne(digits)
        want = [2]
        self.assertEqual(want, got)

    def test_plus(self):
        digits = [1,2,3]
        got = Solution().plusOne(digits)
        want = [1,2,4]
        self.assertEqual(want, got)

    def test_plus_2(self):
        digits = [4,3,2,1]
        got = Solution().plusOne(digits)
        want = [4,3,2,2]
        self.assertEqual(want, got)

    def test_plus_9(self):
        digits = [9]
        got = Solution().plusOne(digits)
        want = [1,0]
        self.assertEqual(want, got)

    def test_plus_999(self):
        digits = [9,9,9]
        got = Solution().plusOne(digits)
        want = [1,0,0,0]
        self.assertEqual(want, got)

    def test_plus_990(self):
        digits = [9,8,9]
        got = Solution().plusOne(digits)
        want = [9,9,0]
        self.assertEqual(want, got)

    def test_plus_988(self):
        digits = [9,8,8]
        got = Solution().plusOne(digits)
        want = [9,8,9]
        self.assertEqual(want, got)
