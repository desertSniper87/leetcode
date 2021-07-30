from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = {i: [] for i in range(len(rooms))}

        for rx, keys in enumerate(rooms):
            graph[rx].extend(keys)

        visited = {i: False for i in range(len(rooms))}
        visited[0] = True
        q = {*graph[0]}

        while q:
            u = q.pop()
            visited[u] = True
            q.update(x for x in graph[u] if not visited[x])

        return all(v for v in visited.values())






if __name__ == '__main__':
    s = Solution()
    input = [
        [[1], [2], [3], []],
        [[1, 3], [3, 0, 1], [2], [0]]
    ]
    for i in input:
        print(s.canVisitAllRooms(i))
