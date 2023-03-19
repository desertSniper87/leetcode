from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)

        bought =  False

        minimum = prices[0]
        maximum = 0
        
        profit = 0

        for i in range(l-1):
            prev = prices[i]
            next = prices[i+1]

            if next > prev:
                bought = True
                maximum = next
                minimum = min(prev, minimum)

            elif bought:
                profit += (maximum - minimum)
                minimum = prev
                bought = False

            else:
                minimum = next

        if bought:
            profit += (maximum-minimum)

        return profit




if __name__ == "__main__":
    s = Solution()
    # print(s.maxProfit([7,1,5,3,6,4]))
    # print(s.maxProfit([1,2,3,4,5]))
    # print(s.maxProfit([1,2,1,4,5]))
    print(s.maxProfit([7,6,4,3,1]))

