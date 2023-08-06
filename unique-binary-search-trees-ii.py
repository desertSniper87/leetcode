from typing import List, Optional
import copy

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
   def __str__(self):
          return f"{self.val}, left={self.left}, right={self.right} || "

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def generate_trees(start, end):
            trees = []
            if start > end:
                trees.append(None)
                return trees

            for i in range(start, end + 1):
                left_trees = generate_trees(start, i - 1)
                right_trees = generate_trees(i + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        trees.append(root)

            return trees

        if n == 0:
            return []

        return generate_trees(1, n)





if __name__ == "__main__":
    s = Solution()
    print(list(map(str, s.generateTrees(3))))
    # list(map(str, s.generateTrees(3)))
