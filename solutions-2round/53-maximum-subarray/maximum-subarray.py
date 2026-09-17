class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur = res = nums[0]

        for i in range(1,len(nums)):
            cur = max(nums[i], cur + nums[i])
            res = max(cur, res) # record the max dp
        return res