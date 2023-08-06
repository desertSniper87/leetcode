class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        memo = {}

        def backtrack(level, current):
            if level == goal:
                if len(set(current)) == n:
                    return 1
                return 0
            
            if (level, tuple(current[-k:])) in memo:
                return memo[(level, tuple(current[-k:]))]

            count = 0
            for i in range(1, n + 1):
                if i not in current[-k:] or k == 0:
                    current.append(i)
                    count = (count + backtrack(level + 1, current)) % MOD
                    current.pop()

            memo[(level, tuple(current[-k:]))] = count
            return count

        return backtrack(0, [])

