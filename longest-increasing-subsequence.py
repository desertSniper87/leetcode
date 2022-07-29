from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        table = [0] * len(nums)

        print(table)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: # Next number is less than previous number
                    table[i] = max(table[i], table[j] + 1)
                # print(i, j, (nums[i], nums[j]), table)

        return max(table) + 1


s = Solution() 

s.lengthOfLIS([10,9,2,5,3,7,101,18])
s.lengthOfLIS([0,1,0,3,2,3])
s.lengthOfLIS([7,7,7,7,7,7,7])




