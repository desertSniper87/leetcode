from itertools import chain
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
