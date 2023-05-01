from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        table = [False for _ in range(l)]


        if l == 1:
            return True

        elif l == 2 and  nums[0] == 0:
            return False
            
        table[l - 1] = True
        table[l - 2] = True

        #  print(start)
        stack = [l - 2]

        while stack:
            start = stack.pop()
            for i in range(nums[start]):
                print(i)
                index = start-i-1
                print(index)
                if not table[index] and index >= 0 and nums[index] + index >= start:
                    print(start, index, nums[index])
                    table[index] = True
                    stack.append(index)


        
        return table[0]

if __name__ == "__main__":
    s = Solution()
    #  print(s.canJump([2,3,1,1,4]))
    #  print(s.canJump([3,2,1,0,4]))
    #  print(s.canJump([0,1]))
    #  print(s.canJump([0,2,3]))
    print(s.canJump([2,0,0]))
