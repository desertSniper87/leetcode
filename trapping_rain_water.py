from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)

        left_max = right_max = [0 for _ in range(length)]

        for ix, i in enumerate(height):
            if ix == 0:
                left_max[ix] = i
            else:
                left_max[ix] = max(i, left_max[ix-1])
            print(ix, i, left_max[ix])

        for jx, j in enumerate(reversed(height)):
            if jx == 0:
                right_max[jx] = height[ix]
                break
            else:
                right_max[jx] = max(height[jx], right_max[jx])


        print(left_max, right_max)

        
