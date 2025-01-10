def solution(budget, classi):
    dp = [[0] * (budget + 1) for _ in range(len(classi))]
    n = len(classi)

    if n == 0 or budget == 0:
        return 0
    
    #Controllo del caso base
    costo_minimo = 0
    for i in range(n):
        costo_minimo+=min(classi[i])
    if costo_minimo > budget:
        return "denaro insufficiente"

    for i in range(1, budget + 1):
        for oggetto in classi[-1]:
            if oggetto <= i:
                dp[-1][i] = max(dp[-1][i], oggetto)

    for classe in range(n - 2, -1, -1):
        for j in range(1, budget + 1):
            for oggetto in classi[classe]:
                if oggetto <= j:
                    dp[classe][j] = max(dp[classe][j], oggetto + dp[classe + 1][j - oggetto])
    
    return dp[0][budget]


print(solution(100,[[8,6,4],[5,10],[1,3,3,7],[50,14,23,8]]))
print(solution(20,[[4,6,8],[5,10],[1,3,5,5]]))
print(solution(5,[[6,4,8],[10,6],[7,3,1,7]]))
