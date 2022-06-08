from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        high, low = l - 1, 0

        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                print("high", high)
                print("nums[high]", nums[high])
                print("mid", mid)
                print("nums[mid]", nums[mid])
                print("low", low)
                print("nums[low]", nums[low])
              
    
                break
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

      firstIndex, lastIndex = mid, mid

      while firstIndex > 0:
        


s = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
s.searchRange(nums, target)
