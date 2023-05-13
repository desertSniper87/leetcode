from typing import Dict, List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        l  = len(questions)
        dp: Dict[int, int] = {}
        def getMostPoints(i):
            if i >= l:
                return 0
            #  print(f"i: {i}, questions[i]: {questions[i]}" ) 

            if i in dp:
                return dp[i]

            dp[i] = max(questions[i][0] + getMostPoints(i+questions[i][1]+1), getMostPoints(i+1))

            return dp[i]

            
        return getMostPoints(0)


if __name__ == "__main__":
    s = Solution()
    print(s.mostPoints([[3,2],[4,3],[4,4],[2,5]]))
    print(s.mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]))
