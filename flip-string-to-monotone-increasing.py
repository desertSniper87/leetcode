class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        num = 0
        for c in s:
            if c == '0':
                ans = min(num, ans + 1)
            else:
                num += 1

            print(c, ans, num)
        return ans

if __name__ == "__main__":
    s = Solution()
    # print(s.minFlipsMonoIncr("00110"))
    #  print(s.minFlipsMonoIncr("010110"))
    #  print(s.minFlipsMonoIncr("00011000"))
    #  print(s.minFlipsMonoIncr("0101100011"))
    print(s.minFlipsMonoIncr("10011111110010111011"))
