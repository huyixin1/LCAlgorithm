class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        least = sys.maxsize
        for i in range(len(prices)):
            least = min(least,prices[i])
            res = max(prices[i] - least, res)

        return res
