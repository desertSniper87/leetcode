class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        elif not sum(nums) and len(set(nums)) == 1:
            return [[0,0,0]]

        nums = sorted(nums)
        l = len(nums)
        res = []

        for m in range(l):
            for n in range(m+2, l):
                if nums[n] == nums[m]:
                    nums[n] = None

        nums = list(filter(lambda x: x is not None, nums))
        l = len(nums)


        for i in range(l):
            for j in range(i+1, l):
                for k in range(j+1, l):
                    item = [nums[i], nums[j], nums[k]]
                    if sum(item) > 0:
                        break
                    elif sum(item) == 0:
                        if res and res[-1] != item or not res:
                            res.append(item)

        return res


        
s = Solution()

# nums = [-1, 0, 1, 2, -1, -4]; print(s.threeSum(nums))
# nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]; print(s.threeSum(nums))
# nums = [0,0,0]; print(s.threeSum(nums))
nums = [0,0,0,0]; print(s.threeSum(nums))
nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]; print(s.threeSum(nums))

