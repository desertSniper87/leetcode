class Solution:
    def minPartitions(self, n: str) -> int:
        y = 0

        print('i, f"{i:b}", y')
        for i in range(1, int(n)):
            y += int(f"{i:b}")
            print(i, f"{i:b}", y)

        return 1

if __name__ == '__main__':
    s = Solution()
    s.minPartitions("10")