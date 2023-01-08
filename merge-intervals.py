from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])

        result = []

        for [i, j] in intervals:
            if not result:
                result.append([i, j])
                continue

            current = result[-1]

            if i <= current[1] and j >= current[1]:
                result[-1] = [current[0], j]

            elif i <= current[1] and j <= current[1]:
                continue

            else:
                result.append([i, j])


        return result


if __name__ == "__main__":
    s = Solution()
    #  print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(s.merge([[1,4],[4,5]]))
    

