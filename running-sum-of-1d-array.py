from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ret = [-1 for _ in range(l)]
        s = 0

        for i in range(l):
            s += nums [i]
            ret[i] = s

        return ret




if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4] ; print(s.runningSum(nums))
    nums = [1,1,1,1,1] ; print(s.runningSum(nums))
