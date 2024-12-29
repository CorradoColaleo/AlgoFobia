class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        elif len(nums)==2:
            return 1
        dp = [float("inf")]*len(nums)
        dp[-1]=0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]!=0:
                dp[i]=1+dp[i+1]
                for j in range(i+2,i+nums[i]+1):
                    if j >=len(nums):
                        break
                    dp[i] = min(dp[i],1+dp[j])
        return dp[0]

        