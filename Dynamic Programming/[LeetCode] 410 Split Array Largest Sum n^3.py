class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[float("inf")]*k for _ in range(n)]
        for i in range(n):
            dp[i][k-1]=sum(nums[i:])
        for i in range(n-2,-1,-1):
            for j in range(k-2,-1,-1):
                for m in range(i+1,n):
                    dp[i][j]=min(dp[i][j],max(sum(nums[i:m]),dp[m][j+1]))
        return dp[0][0]