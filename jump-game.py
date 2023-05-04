from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        table = [False for _ in range(l)]


        if l == 1:
            return True

        elif l == 2 and  nums[0] == 0:
            return False
            
        table[0] = True

        #  print(start)
        stack = [0]

        while stack:
            start = stack.pop()
            if start + nums[start] >= l: 
                return True
            for i in range(nums[start] + start + 1, 0, -1):
                index = start +  i
                if index < l and not table[index] and index - start <= nums[start]:
                    table[index] = True
                    stack.insert(0, index)
                    


        
        return table[l-1]

if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))
    print(s.canJump([0,1]))
    print(s.canJump([0,2,3]))
    print(s.canJump([2,0,0]))
