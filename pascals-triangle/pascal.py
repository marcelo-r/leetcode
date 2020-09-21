from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = {}
        pascal[1] = [1] 
        for i in range(2, numRows+1): 
            pascal[i] = [1] * i 
            row = i - 1 
            pascal[i][1] = row 
            pascal[i][-2] = row 
            mid = [pascal[i-1][j-1] + pascal[i-1][j]  for j in range(2, row-1)]
            pascal[i][2:-2] = mid
        return sorted(pascal.values())

if __name__ == "__main__":
    from pprint import pprint
    pprint(Solution().generate(5))

"""
l = {} 
    ...: for pa, f in zip(range(1, 6), range(6, 2, -1)): 
    ...:     l[pa] = [1] + [x + f for x in range(pa)] 
    ...:     print(l[pa]) 
    ...: print()  
    ...: print(l) 
"""
