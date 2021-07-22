

class Node:
    def __init__(self, val: int) -> None:
        self.val = val

        self.left = None
        self.right = None
        self.up = None
        self.down = None
    
    def assignNeighbor(self, node: Node, direction) -> None:
        if direction == 'up':
            node.up = self.up
            self.up.down = node
        elif direction == 'down':
            node.down = self.down
            self.down.up = node
        elif direction == 'left':
            node.left = self.left
            self.left.right = node
        elif direction == 'right':
            node.right = self.right
            self.right.left = node

class Solution:
    def genGraph(self, grid: List[List[int]]) -> Node:
        start = Node(grid[0].pop(0))

        for row in grid:
            for col in row:
                if col == 1:
                    start.left = Node(0)

        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        