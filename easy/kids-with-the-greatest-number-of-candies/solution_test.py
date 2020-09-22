import unittest

from solution import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        tests = [
            {
                "candies": [2, 3, 5, 1, 3],
                "extraCandies": 3,
                "want": [True, True, True, False, True],
            },
            {
                "candies": [4, 2, 1, 1, 2],
                "extraCandies": 1,
                "want": [True, False, False, False, False],
            },
            {"candies": [12, 1, 12], "extraCandies": 10, "want": [True, False, True]},
            {
                "candies": [1, 1, 1, 1, 1],
                "extraCandies": 1,
                "want": [True, True, True, True, True,],
            },
        ]
        for test in tests:
            with self.subTest(
                candies=test["candies"], extra=test["extraCandies"], want=test["want"]
            ):
                got = Solution().kidsWithCandies(
                    candies=test["candies"], extraCandies=test["extraCandies"]
                )
                self.assertListEqual(test["want"], got)
