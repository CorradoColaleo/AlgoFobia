def solution(n,t,m):
    dim=len(m)
    dp = [float("inf")]*dim
    viaggi = [0]*dim
    dp[0]=m[0]+2*t
    viaggi[0]=1
    for i in range(1,dim):
        for k in range(1,n+1):
            if i-k==-1:
                temp = min(dp[i],m[i]+2*t)   
                if temp!=dp[i]:
                    viaggi[i]=1
                dp[i]=temp
            if i-k>-1:        
                tempoAttesa = 0 if m[i]<= dp[i-k] else m[i]-dp[i-k]
                temp = min(dp[i],tempoAttesa+dp[i-k]+(2*t))
                if temp != dp[i]:
                    viaggi[i]=1+viaggi[i-k]
                dp[i]=temp
            else:
                break
    print(dp[dim-1]-t)
    print(viaggi[dim-1])
    return dp[dim-1]-t,viaggi[dim-1]


solution(2,10,[0,10,20,30,40,50,60,70,80,90])
solution(2,10,[10,30,40])
