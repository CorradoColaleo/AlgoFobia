from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[(float("-inf"), float("inf")) for _ in range(m)] for _ in range(n)]
        dp[-1][-1] = (grid[-1][-1], grid[-1][-1])
        for i in range(n - 2, -1, -1):
            max_val = grid[i][-1] * dp[i + 1][-1][0]
            min_val = grid[i][-1] * dp[i + 1][-1][1]
            dp[i][-1] = (max(max_val, min_val), min(max_val, min_val))        
        for j in range(m - 2, -1, -1):
            max_val = grid[-1][j] * dp[-1][j + 1][0]
            min_val = grid[-1][j] * dp[-1][j + 1][1]
            dp[-1][j] = (max(max_val, min_val), min(max_val, min_val))        
        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                max_down = grid[i][j] * dp[i + 1][j][0]
                min_down = grid[i][j] * dp[i + 1][j][1]
                max_right = grid[i][j] * dp[i][j + 1][0]
                min_right = grid[i][j] * dp[i][j + 1][1]
                max_val = max(max_down, max_right, min_down, min_right)
                min_val = min(max_down, max_right, min_down, min_right)      
                dp[i][j] = (max_val, min_val)    
        max_product = dp[0][0][0]
        return (max_product % (10**9 + 7)) if max_product >= 0 else -1
