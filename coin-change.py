from pprint import pprint
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        _inf = amount + 1

        table = [_inf for _ in range(amount + 1)]
        table[0] = 0


        for target in range(1, amount + 1):
            for coin in coins:
                if target - coin >= 0:
                    table[target] = min(table[target], 1 + table[target - coin])

        return table[amount] if table[amount] != _inf else -1





if __name__ == '__main__':
    s = Solution();
    print(s.coinChange([1, 2, 5], 11))
    print(s.coinChange([1, 10], 11))
    print(s.coinChange([2], 3))
    print(s.coinChange([2], 4))
