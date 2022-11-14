from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordLengthSet = set(map(len, wordDict))

        charPointer = 0
        table = {}

        while charPointer < len(s):
            for l in wordLengthSet: # 4, 4
                for w in list(filter(lambda x: len(x) == l, wordDict)): # leet code
                    if s[charPointer:charPointer+l] == w:
                        print("-")
                charPointer += l

        return False


if __name__ == "__main__":
    sol = Solution()
    s = "leetcode"; wordDict = ["leet","code"]; print(sol.wordBreak(s, wordDict))
