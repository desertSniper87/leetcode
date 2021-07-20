# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMaxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return max(self.getMaxDepth(root.left), self.getMaxDepth(root.right)) + 1

    def deepestLeavesSum(self, root: TreeNode) -> int:
        return self.getDeepestLeaves(root, 0, self.getMaxDepth(root))
        
    def getDeepestLeaves(self, root: TreeNode, h, maxDepth) -> int:
        if root is None:
            return 0
        elif root.left or root.right:
            return self.getDeepestLeaves(root.left, h+1, maxDepth) + self.getDeepestLeaves(root.right, h+1, maxDepth)
        elif root.left is None and root.right is None and h == maxDepth - 1:
            return root.val
        else:
             return 0
        