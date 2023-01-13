from typing import List, Optional


class Node:
    def __init__(self, val: str, pos: int):
        self.left = None
        self.right = None
        self.val = val
        self.position = pos


class Solution:
    def dfs(self, node: Node, visited: set[int]):
        print(f"visiting {node.val}")

        visited.add(node.position)

        if node.left and node.left.val not in visited:
            self.dfs(node.left, visited)

        if node.right and node.right.val not in visited:
            self.dfs(node.right, visited)

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
        self.dfs(root, set())

if __name__ == "__main__":
    s = Solution()
    print(s.longestPath([-1, 0, 0, 1, 1, 2], "abacbe"))
