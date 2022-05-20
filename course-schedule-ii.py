import itertools
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        for preq1, preq2 in itertools.combinations(prerequisites, 2):
            if (preq1[0], preq1[1]) == (preq2[1], preq2[0]):
                return []

        graph = {i: [] for i in range(numCourses)}

        for preq in prerequisites:
            graph[preq[1]].append(preq[0])

        stack = [max(graph, key=(lambda x: len(graph[x])))]
        # stack = [0]
        visited = []

        while stack:
            u = stack.pop(0)

            visited.append(u)
            stack.extend(x for x in graph[u] if x not in visited and x not in stack)

        if not visited:
            return []
        visited.extend(i for i in range(numCourses) if i not in visited)
        return visited


if __name__ == '__main__':
    s = Solution()
    input = [
        # [2, [[1, 0]]],
        # [4, [[1, 0], [2, 0], [3, 1], [3, 2]]],
        # [1, []],
        # [4, [[1, 0], [2, 0], [3, 1], [3, 2]]],
        # [2, []],
        # [2, [[0, 1]]],
        # [2, [[0,1],[1,0]]],
        [3, [[2,0],[2,1]]]
    ]
    for i in input:
        print(s.findOrder(i[0], i[1]))
