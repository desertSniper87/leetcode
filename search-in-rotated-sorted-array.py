from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if right == 1:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                return -1


        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                if nums[mid] > nums[left]:
                    if nums[mid] > target > nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[right] > nums[mid]:
                    if nums[right] > target > nums[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    return -1

        if left == right and nums[left] == target:
            return left


        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [4,5,6,7,0,1,2];print(s.search(nums, 0))
    nums = [4,5,6,7,0,1,2];print(s.search(nums, 6))
    nums = [3,4,5,1,2];print(s.search(nums, 3))
    nums = [11, 13, 15, 17];print(s.search(nums, 15))
    nums = [1,2];print(s.search(nums, 1))
    nums = [2,1];print(s.search(nums, 1))
    nums = [5,1,2,3,4];print(s.search(nums, 4))
    nums = [2,3,4,5,1];print(s.search(nums, 6))
    nums = [1];print(s.search(nums, 1))
    nums = [5,1,2,3,4];print(s.search(nums, 1))
    nums = [3,1];print(s.search(nums, 0))
    nums = [9,1,2,3,4];print(s.search(nums, 5))
