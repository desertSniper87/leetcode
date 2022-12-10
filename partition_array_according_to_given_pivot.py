from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        mid = []

        for n in nums:
            if n < pivot:
                left.append(n)
            elif n > pivot:
                right.append(n)
            else:
                mid.append(n)

        return left + mid + right

if __name__ == "__main__":
    s = Solution()

    print(s.pivotArray([9,12,5,10,14,3,10], 10))
    nums = [-3,4,3,2]; pivot = 2
    print(s.pivotArray(nums, 2))
