DOT = '.'
SLASH = '/'

class Solution:
    def simplifyPath(self, path: str) -> str:
        i, j, l = 0, 0, len(path)
        stack = []

        def handleVal(val):
            if val == '..':
                if stack:
                    stack.pop()
            elif val == '.':
                pass
            elif val: 
                stack.append(val)


        while i < l:
            if path[i] == SLASH:
                if path[j] == SLASH:
                    val = path[j+1:i]
                    handleVal(val)

                j = i
            i += 1
        else:
            val = path[j+1:]
            handleVal(val)


        last_char = path[j+1:i]

        #  if last_char != '':
            #  stack.append(last_char)

        if not stack:
            return '/'

        if len(stack) == 1 and stack[0] == '':
            return '/'

        if stack[0] != '':
            stack.insert(0, '')

        return "/".join(x for x in stack)

if __name__ == "__main__":
    s = Solution()
    print(s.simplifyPath("/home/"))
    print(s.simplifyPath("/home/torsho"))
    print(s.simplifyPath("/home/torsho/atari"))
    print(s.simplifyPath("/../"))
    print(s.simplifyPath("/home//foo/"))
    print(s.simplifyPath("/a/../../b/../c//.//"))
    print(s.simplifyPath("/"))
    print(s.simplifyPath("/... "))
    print(s.simplifyPath("/home"))
    print(s.simplifyPath("/a//b////c/d//././/.."))
    print(s.simplifyPath("/."))
    
    
    
