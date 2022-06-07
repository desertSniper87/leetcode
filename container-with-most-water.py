class Solution:
    def maxArea(self, height: List[int]) -> int:
        print("Hello Wold")class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        
        left = 0
        right = l - 1
        
        max_so_far = 0
        
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            
            print(water)
            
            if water > max_so_far:
                max_so_far = water
                
            while height[left] < height[left+1]:
                print("left")
                left += 1
                break
            
            while height[right] < height[right-1]:
                print("right")
                right -= 1
                break
                
        return max_so_far


                
            
            
            
            
            
            