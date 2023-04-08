from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        l = len(grid[0])
        w = len(grid)

        land = 1
        water = 0

        result = 0

        visited = {}
        for i in range(w):
            for j in range(l):
                visited[(i, j)] = False

        def getNeighbour(node):
            y, x = node
            n = []

            if y > 0:
                n.append((y-1, x))
            if x > 0:
                n.append((y, x-1))
            if y+1 < w:
                n.append((y+1, x))
            if x+1 < l:
                n.append((y, x+1))

            return n

        def getConnectedLands(node) -> int:
            print(f'connected: {node}')
            connected = 0
            isBorder = False
            stack = [node]

            while stack:
                curr = stack.pop()
                print(f'in stack, curr: {curr}')

                if visited[curr]:
                    continue

                visited[curr] = True
                connected += 1

                y, x = curr

                if y == 0 or x == 0 or y == w-1 or x == l-1:
                    connected = 0
                    isBorder = True

                for n in getNeighbour(curr):
                    if grid[n[0]][n[1]] == land and not visited[n]:
                        print('appending')
                        stack.append(n)

            return 0 if isBorder else connected

        for i in range(w):
            for j in range(l):
                node = (i, j)
                content = grid[i][j]

                print(node, content, visited[node])

                if not visited[node] and content == land:
                    result += getConnectedLands(node)

        return result

if __name__ == "__main__":
    s = Solution()
    #  grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    #  print(s.numEnclaves(grid))
    grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    print(s.numEnclaves(grid))
