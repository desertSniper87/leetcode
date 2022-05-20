class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        left = 0
        right = 1
        m = 0
        
        while left < l and right < l:
            buy = prices[left]
            sell = prices[right]
            
            profit = prices[right] - prices[left]
            if profit > m:
                m = profit
            
            if sell < buy: 
                left = right
                right += 1
            
            else:
                right += 1
            
        return m
        
