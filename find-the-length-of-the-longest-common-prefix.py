from typing import List


def get_digits(number):
    digits = []
    while number > 0:
        digits.insert(0, number % 10)
        number //= 10
    return digits


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def get_prefixes(num):
            prefixes = set()
            while num:
                prefixes.add(num)
                num //= 10
            return prefixes

        prefixes1 = set()
        for num in arr1:
            prefixes1.update(get_prefixes(num))

        max_prefix = 0
        for num in arr2:
            while num:
                if num in prefixes1:
                    max_prefix = max(max_prefix, len(str(num)))
                    break
                num //= 10

        return max_prefix


if __name__ == '__main__':
    # print(
    #     Solution().longestCommonPrefix([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
    # )

    print(Solution().longestCommonPrefix([1, 10, 100], [1000]))
