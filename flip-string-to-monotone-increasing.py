class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        first_zeroes = 0

        for i in range(len(s)):
            if s[i] == '1':
                break
            first_zeroes += 1

        s = s[first_zeroes:]

        print(s, first_zeroes)

        last_ones = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                break
            last_ones += 1

        s = s[0:len(s)-last_ones]

        print(s)


        zero_to_one = 0
        one_to_zero = 0


        for i in range(len(s)-1, -1, -1):

            if s[i] == '0':
                zero_to_one += 1
                #  print('not ok')

            if s[i] == '1':
                one_to_zero += 1
                #  print('ok')

        #  print(one_to_zero, zero_to_one)
        return min(one_to_zero, zero_to_one)

if __name__ == "__main__":
    s = Solution()
    #  print(s.minFlipsMonoIncr("00110"))
    #  print(s.minFlipsMonoIncr("010110"))
    #  print(s.minFlipsMonoIncr("00011000"))
    #  print(s.minFlipsMonoIncr("0101100011"))
    print(s.minFlipsMonoIncr("10011111110010111011"))
