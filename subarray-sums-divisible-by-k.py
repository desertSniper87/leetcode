from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0

        l = len(nums)
        for i in range(l):
            for j in range(i, l):
                print(nums[i:j+1])
                if sum(nums[i:j+1]) % k == 0:
                    result += 1

        return result

   
if __name__ == "__main__":
    s = Solution()
    nums = [4,5,0,-2,-3,1]
    print(s.subarraysDivByK(nums, 5))
