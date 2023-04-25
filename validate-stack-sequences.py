from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        i, j, l = 0, 0, len(pushed)
        stack = []
        #  print(f'l -> {l}')
        while i < l:
            #  print(f'i->{i}, j->{j}, stack-> {stack}')
            if stack and stack[-1] == popped[j]:
                #  print('popping' + ' ' + stack[-1])
                stack.pop()
                j += 1

            elif pushed[i] != popped[j]:
                stack.append(pushed[i])
                i += 1
            

            else: 
                #  print("Ignoring")
                i += 1
                j += 1

        else:
            #  print(stack, j)
            while j < l and stack[-1] == popped[j]:
                #  print(f'popping {stack[-1]}')
                stack.pop()
                j += 1


        
        if not stack:
            return True

        return False
            
            

if __name__ == "__main__":
    s = Solution()
    #  print(s.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
    print(s.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))
    print(s.validateStackSequences([0], [0]))
    print(s.validateStackSequences([2,1,0], [1,2,0]))

        
