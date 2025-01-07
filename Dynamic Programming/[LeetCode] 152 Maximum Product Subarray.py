class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [(0, 0)] * len(nums) 
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                dp[i] = (nums[i], nums[i])  
            else:
                prod1 = nums[i] * dp[i + 1][0]
                prod2 = nums[i] * dp[i + 1][1]
                dp[i] = (  
                    max(nums[i], prod1, prod2),  
                    min(nums[i], prod1, prod2)   
                )
        return max(x[0] for x in dp)
