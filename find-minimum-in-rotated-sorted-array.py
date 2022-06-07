from typing import List


class Solution:
    def __init__(self):
        self.nums = None

    def findMin(self, nums: List[int]) -> int:
        self.nums = nums

        l = 0
        r = len(nums) - 1

        if len(nums) < 2:
            return nums[0]

        minimum = self.binaryFindMin(l, r)

        # while l < r:
        return minimum




    def binaryFindMin(self, l, r):
        m = l + (r - l) // 2

        if self.nums[m] < self.nums[m - 1]:
            return min(self.nums[m], self.nums[m - 1])
        elif self.nums[m] > self.nums[m + 1]:
            return min(self.nums[m], self.nums[m + 1])

        l_ = self.binaryFindMin(l, m)
        if l_:
            return l_
        r_ = self.binaryFindMin(m, r)
        if r_:
            return r_



if __name__ == '__main__':
    s = Solution()
    # nums = [4,5,6,7,0,1,2];print(s.findMin(nums))
    # nums = [3,4,5,1,2];print(s.findMin(nums))
    # nums = [11,13,15,17];print(s.findMin(nums))
    # nums = [1,2];print(s.findMin(nums))
    # nums = [2,1];print(s.findMin(nums))
    # nums = [5,1,2,3,4];print(s.findMin(nums))
    nums = [2,3,4,5,1];print(s.findMin(nums))