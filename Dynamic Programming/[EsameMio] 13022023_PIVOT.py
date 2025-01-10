def minCost(n,cuts):
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



# Esempio di utilizzo
if __name__ == "__main__":
    posizioni = [2, 20, 25]
    costo_minimo = minCost(30, posizioni)
    print(f"Il costo minimo totale è: {costo_minimo}")

    posizioni = [4, 5, 7, 8]
    costo_minimo = minCost(10, posizioni)
    print(f"Il costo minimo totale è: {costo_minimo}")

    posizioni = [25, 50, 75]
    costo_minimo = minCost(100, posizioni)
    print(f"Il costo minimo totale è: {costo_minimo}")

    