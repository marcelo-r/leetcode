from typing import List

"""
"candies": [2, 3, 5, 1, 3],
"extraCandies": 3,
"want": [True, True, True, False, True],
"""


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maior = max(candies)
        result = []
        for i in candies:
            result.append(i + extraCandies >= maior)
        return result
