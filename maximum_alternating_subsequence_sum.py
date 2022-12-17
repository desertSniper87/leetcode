from typing import List

"""
:problem: https://leetcode.com/problems/word-subsets/
"""

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}

        def getSum(index: int, even: bool) -> int:
            print('a', index, even)
            if dp.get((index, even)) is not None:
                return dp[(index, even)]

            if index == len(nums) - 1:
                print('b', (-nums[index], nums[index])[even])
                return (-nums[index], nums[index])[even]

            if even:
                print('c')
                evenSum = getSum(index + 1, not even)
                print('e', evenSum)
                dp[(index, even)] = max(nums[index] + evenSum, evenSum)
            else:
                print('d')
                oddSum = getSum(index + 1, not even)
                print('f', oddSum)
                dp[(index, even)] = max(-nums[index] + oddSum, oddSum)

            return dp[(index, even)]

        for i in range(len(nums)):
            # even = not (i % 2)
            dp[(i, True)] = getSum(i, True)

        print(dp)


if __name__ == "__main__":
    s = Solution()
    nums = [4, 2, 5, 3];s.maxAlternatingSum(nums)
    nums =[5,6,7,8] ; s.maxAlternatingSum(nums)
