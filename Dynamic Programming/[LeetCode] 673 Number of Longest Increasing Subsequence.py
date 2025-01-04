class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n
        count = [1] * n
        for i in range(n - 2, -1, -1): 
            for j in range(i + 1, n):  
                if nums[i] < nums[j]:  
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1:
                        count[i] += count[j]  
        max_length = max(dp)
        return sum(c for i, c in enumerate(count) if dp[i] == max_length)
