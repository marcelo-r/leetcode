class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [] 
        for i, j in zip(range(0, n),range(n,2*n)): 
            res.append(nums[i]) 
            res.append(nums[j])
        return res
