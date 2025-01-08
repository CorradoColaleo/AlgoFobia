class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        dp = [[0]*n for _ in range(n)]
        satisfaction.sort()
        dp[0][0]=satisfaction[0]
        for i in range(1,n):
            for j in range(0,n):
                if j==0:
                    dp[i][j]=satisfaction[i]
                else:
                    if i>=j:
                        dp[i][j]=dp[i-1][j-1]+(satisfaction[i]*(j+1))
        return max(dp[-1]) if max(dp[-1]) >0 else 0                  