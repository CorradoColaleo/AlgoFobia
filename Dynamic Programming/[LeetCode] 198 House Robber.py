class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        for i in range(len(nums)):
            if i==0:
                dp[i]=nums[i]
            elif i==1:
                dp[i]=max(dp[i-1],nums[1])
            else:
                dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[len(nums)-1]
        
