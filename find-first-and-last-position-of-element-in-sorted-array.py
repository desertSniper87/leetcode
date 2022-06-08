from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        high, low = l - 1, 0
        found = False

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                print("mid", mid)
                found = True
                break
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        if not found:
            return [-1, -1]

        firstIndex, lastIndex = mid, mid

        while firstIndex >= 0:
            if nums[firstIndex] != target:
                break
            firstIndex -= 1
            print("firstIndex", firstIndex)

        while lastIndex < l:
            if nums[lastIndex] != target:
                break
            lastIndex += 1
            print("lastIndex", lastIndex)

        return [firstIndex + 1, lastIndex - 1]

s = Solution()
print(s.searchRange([1], 1))




