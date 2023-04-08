from typing import List, Tuple 
import collections

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        l = len(grid[0])
        w = len(grid)

        water = 1
        land = 0

        islands = 0

        visited = {}
        enqued = {}
        for i in range(w):
            for j in range(l):
                visited[(i, j)] = False
                enqued[(i, j)] = False

        root = (0, 0)
        queue = collections.deque([root])
        visited[root] = True

        q2 = collections.deque([])

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

        def getConnectedLands(node):
            print(f"connected -> {node}")



            y, x = node
            content = grid[v[0]][v[1]]

            # print(f'{node} -> {getNeighbour(node)}')

            for n in getNeighbour(node):
                if grid[n[0]][n[1]] == land and not visited[n]:
                    q2.append(n)

            for n in getNeighbour(node):
                if grid[n[0]][n[1]] == land and not visited[n]:

                    visited[n] = True

                    y2,x2 = n
                    c2 = grid[n[0]][n[1]]
                    # print(y2, x2)
                    if (y2 == 0 or x2 == 0 or y2+1 == w or x2+1 == l) and c2 == land:
                        print("no way")
                        while q2:
                            v2 = q2.popleft()
                            visited[v2] = True
                            for n3 in getNeighbour(v2):
                                if grid[n3[0]][n3[1]] == land and not visited[n3]:
                                    q2.append(n3)
                                    visited[n3] = True
                        return False

                    # print(f'connected: {n}')
                    return getConnectedLands(n)

            if y > 0 and x > 0 and y+1 < w and x+1 < l and content == land:
                # print(f'returning true -> {node}')
                while q2:
                    # print("q2")
                    v2 = q2.popleft()
                    if not visited[v2]:
                        # print(f'v2: {v2}')
                        visited[v2] =True
                        return getConnectedLands(v2)
                else:
                    return True
            # elif (y == 0 or x == 0 or y+1 == w or x+1 == l) and content == land:
            #     return False
            else:
                print(f'returning false -> {node}')
                return False



        

        while queue:
            v = queue.popleft()

            print(f'visiting {v}')

            content = grid[v[0]][v[1]]

            if content == land:
                q2 = collections.deque([v])
                if not visited[v] and content == land and getConnectedLands(v):
                    print(f'found island: {v}')
                    # print(f'visited: {visited}')
                    islands += 1
                #  print('found land')

            visited[v] = True

            for n in getNeighbour(v):
                if not visited[n] and not enqued[n]:
                    # print(f'appending {n}')
                    queue.append(n)
                    enqued[n] = True


                                                      

        # print(visited)
        return islands

if __name__ == "__main__":
    s = Solution()
    # grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
    # print(s.closedIsland(grid))
    # grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    # grid = [[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]]
    grid = [[0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1],[0,1,1,0,0,0,0,1,1,1,0,1,0,1,1,0,0,1,0,1],[1,1,0,1,0,0,1,1,1,0,0,0,1,0,0,1,0,1,0,0],[0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0],[1,1,0,0,1,0,0,1,1,0,1,1,0,1,1,1,0,0,1,1],[1,1,0,0,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,1],[1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0],[1,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1],[0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,1,0,0,0],[1,1,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,0,1,1],[1,0,0,1,1,1,1,0,1,0,1,1,1,0,0,0,0,1,1,0],[1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,1,1],[0,1,1,0,0,1,1,0,0,1,0,1,1,1,1,1,1,0,0,0],[1,0,0,0,1,1,0,1,1,1,0,0,1,0,1,1,0,1,0,1]]
    print(s.closedIsland(grid))
