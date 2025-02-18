"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(0, length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        # TODO solve using a hash map
        index = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in index:
                pass

if __name__ == "__main__":
    s = Solution().twoSum([-3,-3], -6)
    print(s)
    
