from typing import List, Set

class Solution:
    wordDictLenSet : Set[int]
    s              : str
    wordDict       : List[str]

    def helper(self, i: int):
        print(f"i -> {i}")

        for j in self.wordDictLenSet:

            if i + j > len(self.s):
                break

            print(f"j -> {j}")
            words = filter(lambda x: len(x) == j, self.wordDict)
            for w in words:
                print(f"{self.s[i:i+j]} != {w}")
                if self.s[i:i+j] == w:
                    if i + j == len(self.s):
                        return True
                    return self.helper(i+j)




    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDictLenSet = set(map(len, wordDict))
        self.s = s
        self.wordDict = wordDict

        for i in self.wordDictLenSet:
            r = self.helper(i)

            if r == True:
                return r

        r = self.helper(0)
        if r:
            return True
        return False


if __name__ == "__main__":
    sol = Solution()
    # s = "leetcode"; wordDict = ["leet","code"]; print(sol.wordBreak(s, wordDict))
    # s = "applepenapple"; wordDict = ["apple","pen"] ;  print(sol.wordBreak(s, wordDict))
    # s = "catsandog"; wordDict = ["cats","dog","sand","and","cat"]; print(sol.wordBreak(s, wordDict))
    s = "a"; wordDict = ["a"]; print(sol.wordBreak(s, wordDict))
