from pprint import pprint
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        print(coins)

        n = len(coins)

        table = [[0 for _ in range(0, amount + 1)] for _ in range(n)]

        # pprint(table)

        def getMinCoins(c, t):
            min_coins = 0
            i = len(c) - 1
            while t > 0 and i >= 0:
                if t >= c[i]:
                    t -= c[i]
                    min_coins += 1
                else:
                    i -= 1
            if t == 0:
                return min_coins
            return None

        pprint(table)

        for coin_i in range(len(coins)):
            for target in range(amount + 1):
                m = getMinCoins(coins[:coin_i+1], target)
                if target > 0:
                    m = min(table[coin_i][target-1] + 1, m)
                if coin_i > 0:
                    m = min(table[coin_i-1][target], m)
                table[coin_i][target] = m
                pprint(table)

        return table[n-1][amount]


        # for coin_x, coin in enumerate(coins):
        #     for i in range():
        #         table[coin_x][coin] +=

        # for i in range(n):





if __name__ == '__main__':
    s = Solution();
    # print(s.coinChange([1, 2, 5], 11))
    # print(s.coinChange([2], 3))
    print(s.coinChange([2], 4))
