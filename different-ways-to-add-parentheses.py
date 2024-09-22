from typing import List

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
}


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        print(f"expression: {expression}")
        results = []
        if len(expression) == 0:
            return results

        elif len(expression) == 1 or (
            len(expression) == 2 and expression[0].isdigit()
        ):
            return [int(expression)]

        for ex, e in enumerate(expression):
            print(f"e: {e}")
            if e.isdigit():
                continue

            left_items = self.diffWaysToCompute(expression[:ex])
            right_items = self.diffWaysToCompute(expression[ex + 1 :])
            print(f"left_items: {left_items}, right_items: {right_items}")

            results.extend(
                operations[e](left, right)
                for left in left_items
                for right in right_items
            )
        return results


s = Solution()
# print(s.diffWaysToCompute("2-1-1"))
print(s.diffWaysToCompute("2*3-4*5"))
