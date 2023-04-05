from typing import List 
import math


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = nums[0]
        total = nums[0]
        l = len(nums)

        for i in range(1, l):
            total += nums[i]
            result = max(result, math.ceil(total / (i+1)))
        return result




if __name__ == "__main__":
    s = Solution()
    print(s.minimizeArrayValue([3,7,1,6]))

