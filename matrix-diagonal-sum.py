from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer = 0
        for idx, i in enumerate(mat):
            for jdx, j in enumerate(i):
                if idx == jdx or idx + jdx == len(i) - 1:
                    answer += j

        return answer

if __name__ == "__main__":
    s = Solution()
    mat = [[1,2,3],
           [4,5,6],
           [7,8,9]]
    print(s.diagonalSum(mat))
