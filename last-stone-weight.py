from typing import List
import bisect

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_sorted = sorted(stones)
        print(stones_sorted)

        while len(stones_sorted) > 1:
            x, y = stones_sorted[-2:]
            stones_sorted = stones_sorted[:-2]
            if x != y:
                bisect.insort(stones_sorted, y-x)


        return stones_sorted[0] if stones_sorted else 0



if __name__ == "__main__":
    s = Solution()
    print(s.lastStoneWeight([2,7,4,1,8,1]))
    print(s.lastStoneWeight([1]))
    print(s.lastStoneWeight([3,7,2]))
    print(s.lastStoneWeight([3,7,8]))
    print(s.lastStoneWeight([2,2]))
    

            

        
