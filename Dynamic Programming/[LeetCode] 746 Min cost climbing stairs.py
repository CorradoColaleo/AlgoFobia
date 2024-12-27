class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<=2:
            return min(cost)
        n = len(cost)
        dp = [float("inf")]*n
        dp[-1]=cost[-1]
        for i in range(n-2,-1,-1):
            if i==0:
                dp[i] = min(cost[i]+dp[i+1],cost[i]+dp[i+2],dp[i+1])
            elif i==n-2:
                dp[i] = cost[i]
            else:
                dp[i] = min(cost[i]+dp[i+1],cost[i]+dp[i+2])
        return dp[0]
