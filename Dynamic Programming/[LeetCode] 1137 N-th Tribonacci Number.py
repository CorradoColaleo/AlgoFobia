class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        memo[0]=0
        memo[1]=1
        memo[2]=1
        if n<=2:
            return memo[n]
        res=0
        for i in range(3,n+1):
            res = memo[i-1]+memo[i-2]+memo[i-3]
            memo[i]=res
        return memo[n]