class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(index, current):
            if index == len(nums):
                result.append(current[:])
                return

            for i in range(len(nums)):
                if nums[i] not in current:
                    current.append(nums[i])
                    backtrack(index + 1, current)
                    current.pop()

        if not nums:
            return result

        backtrack(0, [])

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3])) 
    


