class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        dp = [[0] * k for _ in range(n)]  
        for i in range(n):
            dp[i][-1] = sum(nums[i:]) / len(nums[i:])
        for i in range(k - 1): 
            dp[-1][i] = dp[-1][-1]
        for r in range(n - 2, -1, -1):
            for c in range(k - 2, -1, -1):  
                for j in range(r + 1, n):
                    dp[r][c] = max(dp[r][c], (sum(nums[r:j]) / len(nums[r:j]) + dp[j][c + 1]))
        return dp[0][0]  
