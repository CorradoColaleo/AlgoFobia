def catalan(n):
    dp = [0] * (n + 1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        for j in range(0,i):
            dp[i]+=dp[j]*dp[i-1-j]
    return dp[n]

print(catalan(6))
print(catalan(8))