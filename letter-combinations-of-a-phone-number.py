from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
                "0" : "",
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"
                }
        l = len(digits)
        result = []

        def backtrack(i: int, currentString: str):
            if len(currentString) == len(digits):
                result.append(currentString)
                return

            for c in keyboard[digits[i]]:
                backtrack(i+1, currentString + c)


        if digits:
            backtrack(0, "")

        return result



if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
