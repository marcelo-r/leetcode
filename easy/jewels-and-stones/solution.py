class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = {k: True for k in J}
        l = len(S)
        counter = 0
        for si, sj in zip(range(l), range(l-1, 0, -1)):
            if si > sj:
                break
            elif si == sj:
                if S[si] in jewels:
                    counter += 1
            else:
                if S[si] in jewels:
                    counter += 1
                if S[sj] in jewels:
                    counter += 1
        return counter
