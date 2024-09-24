from typing import List


class Solution:
    def lexicalOrderHelper(self, n, i, result):
        if i > n:
            return

        result.append(i)
        for j in range(10):
            self.lexicalOrderHelper(n, i * 10 + j, result)

    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        for i in range(1, 10):
            self.lexicalOrderHelper(n, i, result)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.lexicalOrder(20))
