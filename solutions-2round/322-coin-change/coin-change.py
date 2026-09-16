class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        INF = float("inf")
        dp = [0] + [INF] * amount
        # amount +1 is INF, for invalid output

        for i in range(1,amount+1):
            for c in coins:
                # out of index check
                if i-c >= 0:
                    dp[i] = min(dp[i-c]+1, dp[i])
                
        return dp[amount] if dp[amount] <= amount else -1