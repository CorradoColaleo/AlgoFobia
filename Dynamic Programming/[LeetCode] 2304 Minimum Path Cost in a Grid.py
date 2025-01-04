class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        dp = [[float("inf")] * (nc) for _ in range(nr)]
        if nr==1:
            return min(grid[0])
        dp[-1]=grid[-1]
        for i in range(nr-2,-1,-1):
            for j in range(nc-1,-1,-1):
                for k in range(0,nc):
                    dp[i][j]=min(dp[i][j],grid[i][j]+dp[i+1][k]+moveCost[grid[i][j]][k])
        return min(dp[0])
