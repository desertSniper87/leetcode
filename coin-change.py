from pprint import pprint
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        print(coins)

        n = len(coins)

        table = [[0 for _ in range(0, amount + 1)] for _ in range(n)]

        for coin_x, coin in enumerate(coins):
            for target in range(1, amount + 1):
                print(coin_x, coin, target)
                # Count of solutions including S[j]
                x = table[target - coin][target] if target - coin >= 0 else 0

                # Count of solutions excluding S[j]
                y = table[target][coin_x -1] if coin_x >= 1 else 0
                table[coin_x][target] = x + y

        pprint(table)


if __name__ == '__main__':
    s = Solution();
    print(s.coinChange([1, 2, 5], 11))
