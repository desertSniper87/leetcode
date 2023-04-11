class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if c == '*' and stack:
                stack.pop()
                continue

            
            stack.append(c)

        return "".join(s for s in stack)
