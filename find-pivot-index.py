from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_index  = 0
        right_index = len(nums) - 1

        left_sum  = nums[left_index]
        right_sum = nums[right_index]

        while right_index > left_index:
            #  print(nums[left_index], nums[right_index])
            #  print(left_sum, right_sum)
            print(left_index, right_index)


            if left_sum == right_sum:
                return left_index + 1


            if left_sum >= right_sum:
                right_index -= 1
                right_sum += nums[right_index]
            else:
                left_index  += 1
                left_sum  += nums[left_index]

        return -1

if __name__ == "__main__":
    s = Solution()
    nums = [1,7,3,6,5,6] ; print(s.pivotIndex(nums))
    nums = [1,2,3] ; print(s.pivotIndex(nums))
