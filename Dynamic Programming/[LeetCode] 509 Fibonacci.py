class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        for i in range(0,n+1):
            if i==0:
                memo[i]=0
            elif i==1:
                memo[i]=1
            else:
                memo[i]=memo[i-1]+memo[i-2]
        return memo[n]
        
