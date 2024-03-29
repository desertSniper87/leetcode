# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:


        def isSameTree(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if node1 is None and node2 is None:
                return True
            elif node1 is None and node2 is not None:
                return False
            elif node1 is not None and node2 is None:
                return False

            if isSameTree(node1.left, node2.right) and isSameTree(node1.right, node2.left) and node1.val == node2.val:
                return True
            else:
                return False


        return isSameTree(root.left, root.right)

        


