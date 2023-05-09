from enum import Enum 
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        class Direction(Enum):
            RIGHT = 3
            DOWN = 2
            LEFT = 1
            UP = 0


        i, j = 0, 0
        width = len(matrix[0])
        height = len(matrix)
        cells = width * height

        left_ceil, up_ceil = 0, 0


        direction = Direction.RIGHT

        def rotate():
            nonlocal direction
            if direction == Direction.UP:
                print(f'Rotating from up to right')
                direction = Direction.RIGHT
            else:
                print(f'Rotating from {direction} to {Direction(direction.value - 1)}')
                direction = Direction(direction.value - 1)



        visited = [[False for _ in range(width)] for _ in range(height)]
        #  print(visited)
        trail = []

        while cells:
            # print(i, j)
            print(i, j, matrix[i][j])
            trail.append(matrix[i][j])
            cells -= 1

            if direction == Direction.RIGHT:
                # print(i, j)
                if j == width - 1:
                    up_ceil += 1
                    i += 1
                    rotate()

                else:
                    j += 1


            elif direction == Direction.DOWN:
                if i == height - 1:
                    height -= 1
                    j -= 1
                    rotate()

                else:
                    i += 1


            elif direction == Direction.LEFT:
                if j == left_ceil:
                    left_ceil += 1
                    i -= 1
                    rotate()

                else:
                    j -= 1

            elif direction == Direction.UP:
                if i == up_ceil:
                    width -= 1
                    j += 1
                    rotate()

                else:
                    i -= 1

        return trail

            


if __name__ == "__main__":
    s = Solution()
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # print(s.spiralOrder(matrix))

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(s.spiralOrder(matrix))


