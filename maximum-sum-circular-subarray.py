from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        result = []

        l = len(nums)
        for i in range(l):
            for j in range(i, l):
                if sum(nums[i:j+1]) == 

   
if __name__ == "__main__":
    s = Solution()
    nums = [1,-2,3,-2]
    s.maxSubarraySumCircular(nums)
