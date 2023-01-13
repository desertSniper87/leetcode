from typing import List, Optional

class Node:
    def __init__(self, val:str, pos=0):
      self.left = None
      self.right = None
      self.val = val
      self.pos = pos

class Solution:

    def longestPath(self, parent: List[int], s: str) -> Optional[int]:
        def get_node(node: Optional[Node], position: int):
            if not node:
                return None

            if node.val == position:
                return node

            return get_node(node.left, position) or get_node(node.right, position)

            

        for (val, pos) in zip(s, parent):
            if pos == -1:
                root = Node(val)
                continue
            
            new_node = Node(val)
            #  prev_node = get_node(va






if __name__ == "__main__":
    s = Solution()
    print(s.longestPath([-1,0,0,1,1,2], "abacbe"))

