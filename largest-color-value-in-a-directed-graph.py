from typing import List
from collections import defaultdict
 
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  
        self.V = vertices  
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def neighbor_gen(self, v):
        for k in self.graph[v]:
            yield k
 
    def topoSortUtil(self, v, visited, stack):
 
        working_stack = [(v, self.neighbor_gen(v))]
 
        while working_stack:
            #  print(f"working_stack: {working_stack}") 
            v, gen = working_stack.pop()
            #  print(f"Popping  v: {v}") 
            visited[v] = True
            print(f"stack: {stack}") 
 
            for next_neighbor in gen:
                if not visited[next_neighbor]:  
                    working_stack.append((v, gen))
                    working_stack.append(
                        (next_neighbor, self.neighbor_gen(next_neighbor)))
                    break
            else:
                stack.append(v)
 
    def toposort(self):
        visited = [False]*self.V
 
        stack = []
 
        for i in range(self.V):
            if not(visited[i]):
                self.topoSortUtil(i, visited, stack)
        stack.reverse()
        print(f"stack: {stack} visited: {visited}") 
        return stack

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        g = Graph(len(colors))

        for e in edges:
            g.addEdge(*e)

        print( g.toposort() )
    



if __name__ == "__main__":
    s = Solution()
    #  print(s.largestPathValue("abaca", [[0,1],[0,2],[2,3],[3,4]]))
    print(s.largestPathValue("a", [[0, 0]]))
