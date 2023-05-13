from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = 0

        l = len(nums)
        #  for i in range(l):
            #  if nums[i] < target:
                #  res += 1
        #  else:
            #  nums = nums[:i]

        def getVal(arr) -> bool:
            if max(arr) +  min(arr) <= target:
                return True
            return False

        j = 1
        while j < l:
            i = 0
            while i < l:
                if i+j > l :
                    break
                print(i, j, nums[i:i+j])
                if getVal(nums[i:i+j]):
                    res += 1
                i += 1
            j += 1

        print(res)


if __name__ == "__main__":
    s = Solution()
    nums = [3,5,6,7]; target = 9
    s.numSubseq(nums, target)
