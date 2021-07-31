from typing import List


class Solution:
    def __init__(self):
        self.graph = dict()
        self.visited = dict()

    def DFSUtil(self, temp, v):
        self.visited[v] = True
        temp.append(v)

        for i in self.graph[v]:
            if not self.visited[i]:
                temp = self.DFSUtil(temp, i)
        return temp

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        l = len(isConnected[0])
        self.graph = {i: [] for i in range(l)}
        for rx, row in enumerate(isConnected):
            for cx, col in enumerate(row):
                if rx != cx and col == 1:
                    self.graph[rx].append(cx)

        self.visited = {i: False for i in range(l)}
        cc = []
        for v in range(l):
            if not self.visited[v]:
                temp = []
                cc.append(self.DFSUtil(temp, v))
        return len(cc)


# if __name__ == '__main__':
#     s = Solution()
#     input = [
#         [[1, 1, 0], [1, 1, 0], [0, 0, 1]],
#         [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
#         [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
#     ]
#     for i in input:
#         print(s.findCircleNum(i))
