class Solution:
    def rob(self, nums: list[int]) -> int:
        l = len(nums)
        
        dp = [0] * l
        dp[0] = nums[0]

        if l == 1:
            return nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, l):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return dp[l-1]