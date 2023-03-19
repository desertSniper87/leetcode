from typing import List, Optional

"""
:problem_link: https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
"""

class Node:
    def __init__(self, val: str, pos: int):
        self.left = None
        self.right = None
        self.val = val
        self.position = pos


class Solution:
    def calculate_distance(self, node: Optional[Node]):
        if not node:
            return 0
        # elif node.val == 'c':
        #     print(node.val)

        val = 0

        if node.left and node.val == node.left.val:
            val += self.calculate_distance(node.left)

        if node.right and node.val == node.right.val:
            val += self.calculate_distance(node.right)

        return 1 + val

    def dfs(self, node: Node, visited: set[int], max_distance=0) -> int:
        print(f"visiting {node.val}")

        print(self.calculate_distance(node))

        visited.add(node.position)

        if node.left and node.left.val not in visited:
            max_distance = max(max_distance, self.dfs(node.left, visited, max_distance))

        if node.right and node.right.val not in visited:
            max_distance = max(max_distance, self.dfs(node.right, visited, max_distance))

        return max_distance

    def longestPath(self, parent: List[int], s: str) -> Optional[int]:
        def get_node(node: Optional[Node], position: int):
            if not node:
                return None

            if node.position == position:
                return node

            return get_node(node.left, position) or get_node(node.right, position)

        root = Node('None', 0)

        for i, (val, parent_position) in enumerate(zip(s, parent)):
            if parent_position == -1:
                root = Node(val, i)
                continue

            new_node = Node(val, i)
            prev_node = get_node(root, parent_position)

            if prev_node is None:
                return

            if prev_node.left is None:
                prev_node.left = new_node

            else:
                prev_node.right = new_node

        # print(root)
        return self.dfs(root, set()) + 1

if __name__ == "__main__":
    s = Solution()
    print(s.longestPath([-1, 0, 0, 1, 1, 2], "abacbe"))
