from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)

        bought =  False

        min = 0
        max = 0
        
        profit = 0

        for i in range(l-1):
            prev = prices[i]
            next = prices[i+1]

            if next > prev:
                max = next


            else:
                profit += (max - min)
                min = -1

        return profit




if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([1,2,3,4,5]))

