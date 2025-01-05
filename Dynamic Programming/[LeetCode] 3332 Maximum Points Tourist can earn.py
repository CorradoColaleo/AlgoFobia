class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [[float("-inf")]*n for _ in range(k)]
        if k == 1:
            for i in range(n):
                for j in range(n):
                    dp[0][i] = max(dp[0][i], stayScore[0][i], travelScore[i][j])
        else:
            #Inizializzo l'ultima riga
            for i in range(n):
                for j in range(n):
                    dp[-1][i] = max(dp[-1][i], stayScore[-1][i], travelScore[i][j])
            
            for i in range(k-2,-1,-1):
                for j in range(n-1,-1,-1):
                   for m in range(n):
                        dp[i][j] = max(dp[i][j], stayScore[i][j] + dp[i+1][j], travelScore[j][m]+dp[i+1][m])
        return max(dp[0])