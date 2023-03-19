# Definition for a binary tree node.

null = None

from typing import Optional, List

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

class Solution:

    result = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result.append(root.val)

        if root.left:
            self.preorderTraversal(root.left)

        if root.right:
            self.preorderTraversal(root.right)

        return self.result



if __name__ == "__main__":
    s = Solution()

    #  print(s.preorderTraversal([1,null,2,3]))
