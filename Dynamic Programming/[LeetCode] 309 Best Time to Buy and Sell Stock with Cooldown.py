class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        elif len(prices)==0:
            return max(0,prices[1]-prices[0])
        n = len(prices)
        dp = [float("-inf")]*n
        dp[-1]=0
        dp[-2]=max(0,prices[-1]-prices[-2])
        for i in range(n-3,-1,-1):
            for j in range(i+1,n):
                if j+2>=n:
                    dp[i]=max(0,dp[i],prices[j]-prices[i])
                else:
                    dp[i] = max(0,dp[i],prices[j]-prices[i]+dp[j+2])
                dp[i]=max(dp[i],dp[i+1])
        return dp[0]
            
        