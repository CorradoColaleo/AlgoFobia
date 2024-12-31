class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 0:
            return 0
        elif n==2:
            return 1
        memo = [0]*(n+1)
        memo[1]=1
        memo[2]=1
        for i in range(3,n+1):
            j = 1
            for num in range(i-1,-1,-1):
                if num>=j:
                    memo[i] = max(memo[i],num*j, memo[num]*j,memo[num]*memo[j],num*memo[j])
                else:
                    break
                j+=1
            print("memo",i,"=",memo[i])
        return memo[n]


    