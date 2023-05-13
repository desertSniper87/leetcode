from typing import Any, List 

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        #  dp: List[Any] = [[None for _ in range(l2)] for _ in range(l1)]
        dp = {}

        def getUncrossedLine(i: int, j: int) -> int:
            if i == l1 or j == l2:
                print(f"i: {i} j: {j} --- reached end")
                return 0

            elif (i, j) in dp:
                print(f"i: {i} j: {j} {nums1[i]}, {nums2[j]} --- memoized")
                return dp[(i, j)]

            elif nums1[i] == nums2[j]:
                print(f"i: {i} j: {j} {nums1[i]}, {nums2[j]} --- matched")
                dp[(i, j)]= 1 + getUncrossedLine(i+1, j+1)

            else:
                print(f"i: {i} j: {j} {nums1[i]}, {nums2[j]} --- not matched")
                dp[(i, j)]= max(getUncrossedLine(i, j+1), getUncrossedLine(i+1, j))

            return dp[(i, j)]

            


        return getUncrossedLine(0, 0)

if __name__ == "__main__":
    s = Solution()
    nums1 = [2,5,1,2,5]; nums2 = [10,5,2,1,5,2]
    print(s.maxUncrossedLines(nums1, nums2))
    nums1 = [1,4,2]; nums2 = [1,2,4]
    print(s.maxUncrossedLines(nums1, nums2))


