from typing import List


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        result: List[TreeNode] = []

        if n < 1:
            return []
        if n == 1:
            return [TreeNode(0)]

        for left_sbtree_n in range(n):
            left_subtree = self.allPossibleFBT(left_sbtree_n)
            right_subtree = self.allPossibleFBT(n - left_sbtree_n)

            for left_treenode in left_subtree:
                for right_treenode in right_subtree:
                    result.extend([left_treenode, right_treenode])

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.allPossibleFBT(2))





