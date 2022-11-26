from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        table = [0] * (l + 1)

        table[1] = nums[0]

        for i in range (2, l+1):
            table[i] = max(nums[i-1] + table[i-2], table[i-1])

        return table[-1]


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,1]; print(s.rob(nums))
    nums = [2,7,9,3,1]; print(s.rob(nums))
    nums = [1] ; print(s.rob(nums))
