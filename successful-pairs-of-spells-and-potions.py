from typing import List
from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions = sorted(potions)
        l = len(potions)
        for s in spells:
            x = success / s
            pos = bisect_left(potions, x)
            res.append(l - pos)

        return res



if __name__ == "__main__":
    s = Solution()
    spells = [5,1,3]; potions = [1,2,3,4,5]; success = 7
    print(s.successfulPairs(spells, potions, success))
