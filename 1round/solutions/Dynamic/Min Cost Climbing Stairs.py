class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)

        dp[0] = cost[0] # first step costs
        dp[1] = cost[1] # cost.length >= 2
        if len(cost) == 2:
            return min(dp[1], dp[0])

        for i in range(2,len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return min(dp[len(cost)-1],dp[len(cost)-2])