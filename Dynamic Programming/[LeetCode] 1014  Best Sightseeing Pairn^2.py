class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        if len == 2:
            return values[0]+values[1]-1
        n = len(values)
        dp = [0]*n
        dp[-1]=float("-inf")
        dp[-2]=values[-2]+values[-1]-1
        for i in range(n-3,-1,-1):
            for j in range(i+1,n):
                temp = values[i]+values[j]+i-j
                dp[i] = max(dp[i],temp)
            dp[i]=max(dp[i],dp[i+1])
        return dp[0]