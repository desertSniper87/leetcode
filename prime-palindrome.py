import math


class Solution:
    def isPrime(self, n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def isPalindrome(self, n: int) -> bool:
        if n == 0:
            return False
        elif n < 10:
            return True
        else:
            s = str(n)
            length = len(s)
            for i in range(0, int(length / 2)):
                if s[i] != s[length - i - 1]:
                    return False
            return True

    def primePalindrome(self, n: int) -> int:
        while True:
            if self.isPalindrome(n) and self.isPrime(n):
                return n
            else:
                n += 1
