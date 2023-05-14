from typing import List
from math import gcd
from queue import PriorityQueue

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        q = PriorityQueue()
        count = {}

        for ix, i in enumerate(nums):


            if i not in count:
                count[i] = 0
            count[i] +=1


            for jx, j in enumerate(nums[ix+1:]):
                deno = gcd(i, j)
                q.put((-deno, (i, j, deno)))
                print(i, j, "-->", deno)

        result = []
        taken = 0
        while not q.empty() or taken != len(nums):
            _, (v1, v2, deno) = q.get()
            if count[v1] != 0 and count[v2] != 0:
                print(v1, v2, deno)
                result.append(deno)

                count[v1] -= 1
                count[v2] -= 1

                taken += 2


        result.sort(reverse=False)
        print(result)
        return sum(list(x * y for x, y in list(zip(result, [i for i in range(1, len(result)+1)]))))




            
            


if __name__ == "__main__":
    s = Solution()
    #  print(s.maxScore([1,2]))
    #  print(s.maxScore([3,4,6,8]))
    #  print(s.maxScore([1,2,3,4,5,6]))
    #  print(s.maxScore([415,230,471,705,902,87]))
    print(s.maxScore([9,17,16,15,18,13,18,20]))
