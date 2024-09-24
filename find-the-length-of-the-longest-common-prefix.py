import math
from typing import List


def get_digits(number):
    digits = []
    while number > 0:
        digits.insert(0, number % 10)
        number //= 10
    return digits


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arrset1 = set(str(x) for x in arr1)
        arrset2 = set(str(x) for x in arr2)

        def len_(a):
            return math.floor(math.log10(a)) + 1

        res = 0

        for a1, a2 in [(a1, a2) for a1 in arrset1 for a2 in arrset2]:
            z = min(len(a1), len(a2))
            i = 0
            while z:
                # print(f'{a1[i]} {a2[i]}')
                if a1[i] == a2[i]:
                    i += 1
                    z -= 1
                else:
                    break

            res = max(i, res)

        return res


if __name__ == '__main__':
    # print(
    #     Solution().longestCommonPrefix([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
    # )

    print(Solution().longestCommonPrefix([1, 10, 100], [1000]))
