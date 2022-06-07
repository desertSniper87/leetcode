from typing import List


class Solution:
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)

if __name__ == '__main__' :
    s = Solution()
    nums = [2,3,-2,4]; print(s.maxProduct(nums))
    # nums = [-2,0,-1]; print(s.maxProduct(nums))
    # nums = [-3,-1,-1]; print(s.maxProduct(nums))
    # nums = [0,2]; print(s.maxProduct(nums))
    # nums = [3,-1,4]; print(s.maxProduct(nums))
    # nums = [3,-1,4, -1]; print(s.maxProduct(nums))