from typing import List


class Solution:
    def lexicalOrderHelper(self, n, i, result=[]):
        result.append(i)
        for j in range(10):
            z = i * 10 + j
            if z < n:
                result.append(z)

            else:
                break

        return result

    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        for i in range(1, n):
            self.lexicalOrderHelper(n, i, result)

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.lexicalOrder(11))
