"""
:problem_link: https://leetcode.com/problems/minimum-path-sum/
"""
from typing import List
from math import inf


class Solution:
    def minPathSum(self, grid: List[List[int]]):
        h = len(grid)
        l = len(grid[0])
        table = [[inf for _ in range(l)] for _ in range(h)]

        def getPathSum(i: int, j: int) -> int | float:
            #  print(i, j)
            #  print('d')
            #  print('==')
            #  [print(a) for a in table]
            #  print('==')
            
            if i == h or j == l:
                #  print('a')
                return inf
                #  print('e', i, j)

            if i == h - 1 and j == l - 1:
                #  print(i, j, l, grid[i][j])
                table[i][j] = grid[i][j]
                #  print('b')

            elif table[i][j] == inf:
                #  print(i, j)
                table[i][j] = grid[i][j] + min(getPathSum(i+1, j), getPathSum(i, j+1))
                #  print(table)

                #  print('c')
            return table[i][j]


        return getPathSum(0, 0)





if __name__ == "__main__":
    s = Solution()
    #  grid = [[1,3,1],[1,5,1],[4,2,1]] ; print(s.minPathSum(grid))
    #  grid = [[1,2,3],[4,5,6]] ; print(s.minPathSum(grid))

    grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
    print(s.minPathSum(grid))

