from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i = 0
        j = 1
        c = 0
        limit = len(nums)
        while True:
            if j >= limit:
                i+=1
                j=i
            if i >= limit:
                break
            if nums[i] == nums[j]:
                if i < j:
                    c += 1
            j+=1
        return c
