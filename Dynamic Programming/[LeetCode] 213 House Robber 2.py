class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = [0]*(len(nums)-1)
        dp2 = [0]*(len(nums)-1)
        
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        
        def helper(nums: List[int], dp: List[int]) -> int:
            for i in range(len(nums)):
                if i==0:
                    dp[i]=nums[i]
                elif i==1:
                    dp[i]=max(dp[i-1],nums[1])
                else:
                    dp[i]=max(dp[i-1],dp[i-2]+nums[i])
            return dp[len(nums)-1]

        r1 = helper(nums[1:],dp1)
        r2 = helper(nums[:-1],dp2)
        return max(r1,r2)
    
        