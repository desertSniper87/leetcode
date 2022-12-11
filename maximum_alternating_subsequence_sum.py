from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}

        def getSum(index: int, even: bool) -> int:
            if dp.get((index, even)) is not None:
                return dp[(index, even)]

            if index == len(nums) - 1:
                return nums[index]

            if even:
                evenSum = getSum(index + 1, not even)
                dp[(index, even)] = max(nums[index] + evenSum, evenSum)
            else:
                oddSum = getSum(index + 1, even)
                dp[(index, even)] = max(-nums[index] + oddSum, oddSum)

            return dp[(index, even)]

        for i in range(len(nums)):
            even = not (i % 2)
            dp[(i, even)] = getSum(i, even)

        print(dp)


if __name__ == "__main__":
    s = Solution()
    nums = [4, 2, 5, 3];s.maxAlternatingSum(nums)
    nums =[5,6,7,8] ; s.maxAlternatingSum(nums)
