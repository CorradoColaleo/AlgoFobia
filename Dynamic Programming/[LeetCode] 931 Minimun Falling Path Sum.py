class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[float("inf")]*m for _ in range(n)]
        for i in range(m):
            dp[-1][i]=matrix[-1][i]
        for i in range(n-2,-1,-1):
            for j in range(m-1,-1,-1):
                if j+1<m and j-1>=0:
                    dp[i][j] = matrix[i][j] + min(dp[i+1][j+1],dp[i+1][j],dp[i+1][j-1])
                elif j+1<m and j-1<0:
                    dp[i][j] = matrix[i][j] + min(dp[i+1][j+1],dp[i+1][j])
                elif j+1>=m and j-1>=0:
                    dp[i][j] = matrix[i][j] + min(dp[i+1][j],dp[i+1][j-1])
                else:
                    dp[i][j] = matrix[i][j] + dp[i+1][j]
        return min(dp[0])
