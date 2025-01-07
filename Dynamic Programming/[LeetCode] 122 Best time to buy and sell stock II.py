class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0]*n
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if j+1<n:
                    dp[i] = max(dp[i],(prices[j]-prices[i])+dp[j+1])
                else:
                    dp[i] = max(dp[i],(prices[j]-prices[i]))
            dp[i]=max(dp[i],dp[i+1])
        return dp[0]