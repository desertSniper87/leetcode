class Solution:
    def getSubStrCount(self, s: str):
        l = len(s)
        i = 0
        res = 0
        for j in range(1, l):
            #  print(i, j, s[i:j], s[j])
            if s[j] in s[i:j] or s[i] == s[j]:
                i = j
                res += 1

        return res + 1
                



    def partitionString(self, s: str) -> int:
        #  return self.getSubStrCount(s)
        #  return self.getSubStrCount(s[::-1])
        return min(self.getSubStrCount(s), self.getSubStrCount(s[::-1]))


if __name__ == "__main__":
    s = Solution()
    print(s.partitionString("abacaba"))
    print(s.partitionString("ssssss"))
    print(s.partitionString("yzubfsiypfrepcfftiov"))
