from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        DP
        :param nums: int
        :return: int
        """
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        m = dp[0]

        for i in range(1, n):
            if dp[i-1] > 0:
                dp[i] = nums[i] + dp[i-1]
            else:
                dp[i] += nums[i]
            m = max(m, dp[i])

        return m


    def maxSubArrayGreedy(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_sum = 0

        for i in range(len(nums)):
            max_sum += nums[i]

            if max_sum > max_so_far:
                max_so_far = max_sum

            if max_sum < 0:
                max_sum = 0


        return max_so_far



if __name__ == '__main__' :
    s = Solution()
    nums = [5, 4, -1, 7, 8]; print(s.maxSubArray(nums))
    nums = [-2,1,-3,4,-1,2,1,-5,4]; print(s.maxSubArray(nums))
    nums = [1]; print(s.maxSubArray(nums))
    nums = [-1]; print(s.maxSubArray(nums))