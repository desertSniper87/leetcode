class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = {}

        def dfs(i):
            if i > high:
                return 0

            if i in dp:
                return dp[i]

            dp[i] = 1 if i >= low else 0
            dp[i] += dfs(i + zero) + dfs (i + one)

            return dp[i] % mod


        return dfs(0)



if __name__ == "__main__":
    s = Solution()
    #  low = 3; high = 3; zero = 1; one = 1
    #  s.countGoodStrings(low, high, zero, one)
    #  low = 3; high = 4; zero = 2; one = 2
    #  print(s.countGoodStrings(low, high, zero, one))
    low = 2; high = 3; zero = 1; one = 2
    print(s.countGoodStrings(low, high, zero, one))
