class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                for m in range(1, k + 1):
                    if j - m >= 0:
                        dp[i][j] += dp[i - 1][j - m]
        return dp[n][target] % (10**9 + 7)


