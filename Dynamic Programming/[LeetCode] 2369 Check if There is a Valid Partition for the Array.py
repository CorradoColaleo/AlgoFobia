class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return False
        if len(nums)==2:
            if (nums[0]==nums[1]):
                return True
            else:
                return False
        if len(nums)==3:
            if (nums[0]==nums[1] and nums[1]==nums[2]) or (nums[0]==nums[1]-1 and nums[1]==nums[2]-1):
                return True
            else:
                return False
        dp = [False] * len(nums)
        if nums[-2]==nums[-1]:
            dp[-2]=True
        for i in range(len(nums)-3,-1,-1):
            if nums[i]==nums[i+1]:
                if dp[i+2]==True:
                    dp[i]=True
            if (nums[i]==nums[i+2] and nums[i+1]==nums[i+2]) or (nums[i]==nums[i+1]-1 and nums[i+1]==nums[i+2]-1):
                if i+3 >= len(nums) or dp[i+3]==True:
                    dp[i]=True
        return dp[0]

        
        