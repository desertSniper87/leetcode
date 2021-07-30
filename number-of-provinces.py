from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        l = len(isConnected[0])
        graph = {i: [] for i in range(l)}
        for rx, row in enumerate(isConnected):
            for cx, col in enumerate(row):
                if rx != cx and col == 1:
                    graph[rx].append(cx)

        visited = {i: False for i in range(l)}
        stack = [0]
        visited[0] = True
        cc = []

        while stack:
            u = stack.pop(-1)
            visited[u] = True
            cc.append(u)

            v = graph[u]

            for v_ in v:
                if not visited[v_]:
                    stack.append(v_)

            print(cc)
        print('=======')




if __name__ == '__main__':
    s = Solution()
    input = [
        [[1,1,0],[1,1,0],[0,0,1]],
        [[1,0,0],[0,1,0],[0,0,1]],
        [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    ]
    for i in input:
        print(s.findCircleNum(i))
