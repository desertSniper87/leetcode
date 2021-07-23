# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return str(self.val)
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder.pop(0))
        while preorder:
            val = preorder.pop(0)
            if val < root.val:
                root.left = self.getNode(root.left, val)
            else:
                root.right = self.getNode(root.right, val)

        return root

    def getNode(self, node: TreeNode, val: int) -> TreeNode:
        newNode = TreeNode(val)
        if node is None:
            return newNode
        else:
            if val < node.val:
                node.left = self.getNode(node.left, val)
            else:
                node.right = self.getNode(node.right, val)

        return node


                


