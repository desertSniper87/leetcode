from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {x: [] for x in range (n)}
        for e in edges:
            graph[e[1]].append(e[0])

        return list(map (lambda x: x[0], (list(filter(lambda x: x[1] == [], graph.items())))))


if __name__ == '__main__':
    s = Solution()
    print(s.findSmallestSetOfVertices(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))
    print(s.findSmallestSetOfVertices(5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))
