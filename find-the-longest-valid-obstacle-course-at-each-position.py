from typing import List

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        l = len(obstacles)
        result = [1 for _ in range(l)]

        maxVal = {}
        def setMaxVal(k, v):
            if not maxVal.get(k):
                maxVal[k] = v
            else:
                maxVal[k] = max(maxVal[k], v)


        for i in range(1, l):
            if maxVal.get(obstacles[i]):
                result[i] = maxVal[max([key for key in maxVal if key <= obstacles[i]], key=maxVal.get)] + 1
            elif obstacles[i] >= obstacles[i-1]:
                result[i] = result[i-1] + 1

            setMaxVal(obstacles[i], result[i])

        return result



if __name__ == "__main__":
    s = Solution()
    print(s.longestObstacleCourseAtEachPosition([1,2,3,2]))
    print(s.longestObstacleCourseAtEachPosition([2,2,1]))
    print(s.longestObstacleCourseAtEachPosition([3,1,5,6,4,2]))
    print(s.longestObstacleCourseAtEachPosition([5,1,5,5,1,3,4,5,1,4]))
