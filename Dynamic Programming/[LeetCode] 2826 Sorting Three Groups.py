class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = dp2 = dp3 = 0
        for num in nums:
            new_dp1 = dp1 + (num != 1)
            new_dp2 = min(dp1, dp2) + (num != 2)
            new_dp3 = min(dp1, dp2, dp3) + (num != 3)
            dp1, dp2, dp3 = new_dp1, new_dp2, new_dp3       
        return min(dp1, dp2, dp3)
