from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        
        left = 0
        right = l - 1
        
        max_so_far = 0
        
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            
            if water > max_so_far:
                max_so_far = water

            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
                
                
        return max_so_far

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))


                
            
            
            
            
            
            
