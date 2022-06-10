from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]



if __name__ == '__main__':
    s = Solution()
    # nums = [4,5,6,7,0,1,2];print(s.findMin(nums))
    # nums = [3,4,5,1,2];print(s.findMin(nums))
    nums = [11,13,15,17];print(s.findMin(nums))
    # nums = [1,2];print(s.findMin(nums))
    # nums = [2,1];print(s.findMin(nums))
    # nums = [5,1,2,3,4];print(s.findMin(nums))
    # nums = [2,3,4,5,1];print(s.findMin(nums))