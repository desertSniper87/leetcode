from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        table = [0] * (len(nums) + 1)

        print(table)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] > nums[i]:
                    table[i] = table[j] + 1
                print(table)

        return max(table)


s = Solution() 

s.lengthOfLIS([10,9,2,5,3,7,101,18])




