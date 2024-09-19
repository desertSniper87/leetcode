from typing import List


class Node:
    def __init__(self, value):
        self.operator = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.operator) + " " + str(self.left) + " " + str(self.right)


class Solution:
    def build_tree(self, expression):
        token_queue = []
        operator_stack = []
        operators = set(["+", "-", "*", "/"])

        for char in expression:
            if char in operators:
                operator_stack.append(char)
            else:
                token_queue.append(char)

        for operator in operator_stack:
            left = token_queue.pop(0)
            right = token_queue.pop(0)
            print(f"left: {left}, right: {right}, operator: {operator}")
            node = Node(operator)
            node.left = left
            node.right = right
            token_queue.append(node)

            # else:
            #     token_queue.append(char)

        return token_queue[0] if token_queue else None

    def print_tree(self, node, level=0):
        if node is not None:
            print("  " * level + str(node.value))
            self.print_tree(node.left, level + 1)
            self.print_tree(node.right, level + 1)

    def diffWaysToCompute(self, expression: str) -> List[int]:
        pass


s = Solution()
# s.build_tree("3+4*2-1")
s.build_tree("2-1-1")
