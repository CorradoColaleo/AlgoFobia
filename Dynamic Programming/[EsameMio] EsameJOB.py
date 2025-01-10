def solution(jobs):
    jobs.sort(key=lambda x: x[1])  # Ordina i job per tempo di fine
    n = len(jobs)
    
    if n == 0:
        return 0
    
    dp = [0] * n  # dp[i] rappresenta il beneficio massimo considerando i job fino all'indice i
    
    # Calcola il beneficio massimo per ogni job
    for i in range(n):
        # Caso base: il beneficio del job corrente
        include_benefit = jobs[i][2]
        
        # Trova il job precedente che non si sovrappone
        for k in range(i - 1, -1, -1):
            if jobs[k][1] <= jobs[i][0]:  # Se il job k non si sovrappone al job i
                include_benefit += dp[k]
                break
        
        # Confronta includendo o escludendo il job corrente
        dp[i] = max(dp[i - 1] if i > 0 else 0, include_benefit)
    
    # Il beneficio massimo si trova nell'ultima cella di dp
    return dp[-1]
