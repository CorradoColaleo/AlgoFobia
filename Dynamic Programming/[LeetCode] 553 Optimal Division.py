class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return f"{nums[0]}/{nums[1]}"
        dp = [[float('inf'), float('-inf')] for _ in range(n)]
        dp[-1] = (nums[-1], nums[-1])
        dp[-2] = (nums[-2] / nums[-1], nums[-2] / nums[-1])
        for i in range(n - 3, -1, -1):
            temp = nums[i]
            for j in range(i + 1, n):
                dp[i] = (
                    min(dp[i][0], temp / dp[j][1]),  
                    max(dp[i][1], temp / dp[j][0])  
                )
            temp = temp/nums[j]
        result = f"{nums[0]}/(" + "/".join(map(str, nums[1:])) + ")"
        return result