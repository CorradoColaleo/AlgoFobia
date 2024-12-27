def solution(classi,budget):

    #definizioni
    n = len(classi)
    dp = [0]*len(classi)

    #caso base
    if n>0:
        massimo = max(classi[-1])
        if massimo <= budget:
            dp[-1] = massimo 
        else:
            return "denaro insufficiente"

    #codice operativo
    for i in range(n-2,-1,-1):
        c = classi[i]
        nl = len(c)
        counter_di = 0
        for j in range(nl):
            if c[j] + dp[i+1] > budget:
                counter_di+=1
            else:
                dp[i] = max(dp[i],c[j]+dp[i+1])
        if counter_di == nl:
            return "denaro insufficiente"

    return dp[0]

print(solution([(8,6,4),(5,10),(1,3,3,7),(50,14,23,8)],100))
print(solution([(4,6,8),(5,10),(1,3,5,5)],20))
print(solution([(6,4,8),(10,6),(7,3,1,7)],5))


