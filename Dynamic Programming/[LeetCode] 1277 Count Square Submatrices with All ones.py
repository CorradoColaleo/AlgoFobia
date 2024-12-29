class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        # Inizializzo la matrice DP
        dp = [[0 for _ in range(m)] for _ in range(n)]
        total_squares = 0
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        # Se siamo nel bordo, il massimo quadrato è dato dal valore stesso
                        dp[i][j] = 1
                    else:
                        # Calcolo il lato massimo del quadrato che termina in (i, j)
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    # Aggiungo il numero di quadrati con vertice in (i, j)
                    total_squares += dp[i][j]
        
        return total_squares