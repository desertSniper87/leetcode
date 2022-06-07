class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = {x: 0 for x in range (3)}
        for n in nums:
            res[n] += 1
            
        # print(res)
        i = 0
        for r in res:
            for _ in range(res[r]):
                nums[i] = r
                i += 1