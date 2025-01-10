class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + cuts + [n]
        cuts.sort()
        m = len(cuts) 
        dp = [[0] * m for _ in range(m)]
        for i in range(m - 1, -1, -1):  
            for j in range(i + 1, m):
                mini = float("inf")
                for k in range(i + 1, j):
                    cost = cuts[j] - cuts[i] + dp[i][k] + dp[k][j]
                    mini = min(mini, cost)
                dp[i][j] = mini if mini != float("inf") else 0  
        return dp[0][m - 1]
