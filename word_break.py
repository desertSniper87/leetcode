from typing import List, Set

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                # print(dp, s[i:i+len(word)], word, i+len(word))
                dp[i] = (s[i:i+len(word)] == word) and dp[i+len(word)]
                if dp[i]:
                    break
            #  print(dp)

        return dp[0]


if __name__ == "__main__":
    sol = Solution()
    s = "leetcode"; wordDict = ["leet","code","neet"]; print(sol.wordBreak(s, wordDict))
    # s = "leetcode"; wordDict = ["leet","code"]; print(sol.wordBreak(s, wordDict))
    # s = "applepenapple"; wordDict = ["apple","pen"] ;  print(sol.wordBreak(s, wordDict))
    # s = "catsandog"; wordDict = ["cats","dog","sand","and","cat"]; print(sol.wordBreak(s, wordDict))
    #  s = "a"; wordDict = ["a"]; print(sol.wordBreak(s, wordDict))
