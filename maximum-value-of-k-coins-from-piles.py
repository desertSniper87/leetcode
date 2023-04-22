from typing import List

def fillPrefixSum(arr): 
    n = len(arr)
    
    prefixSum = [0 for _ in range(n)]
    prefixSum[0] = arr[0]
  
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + arr[i]

    return prefixSum

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        for pile_i, pile in enumerate(piles):
            piles[pile_i] = pile[:k]

        for pile in piles:
            print(f"pile: {pile}", fillPrefixSum(pile))

        

if __name__ == "__main__":
    s = Solution()
    print(s.maxValueOfCoins([[1,100,3],[7,8,9]], 2))
    print(s.maxValueOfCoins([[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], 7))
    print(s.maxValueOfCoins([[1,100,3],[7,8,9],[1,10,100]], 3))
