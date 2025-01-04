class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
       
        n = len(nums)
 
        mod  = 2
 
        sums =sum(nums)
 
        if target < -sums or target > sums:
            return 0
 
        dp = [[0 for _ in range(-sums,sums+1)] for _ in range(2)]
 
        if nums[0] == 0:
            dp[0][sums] = 2  # Due modi: +0 e -0
        else:
            dp[0][sums - nums[0]] = 1
            dp[0][sums + nums[0]] = 1
 
        for k in range(1,n):
 
            for j in range(-sums,2*sums+1):
 
                i = k%mod
                p = (k-1)%mod
                dp[i][j] = 0
 
                if j-nums[k] >=0:
                   
                    dp[i][j] += dp[p][j-nums[k]]
 
                if j+nums[k] <=2*sums:
                    dp[i][j] += dp[p][j+nums[k]]
 
       
        return dp[(n-1)%mod][sums+target]