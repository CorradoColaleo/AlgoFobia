class Solution:
    def divisorGame(self, n: int) -> bool:
        if n==2:
            return True
        if n==1:
            return False
        memo = {}
        memo[1]=True
        memo[2]=True
        def solution(memo,n):
            if n in memo:
                return memo[n]
            done = False
            i=1
            while done is False and ((n-i)>0):
                if (n%i==0):
                    done = True if (solution(memo,n-i) is False) else False
                i+=1
            memo[n]=done
            return done
        solution(memo,n)
        return memo[n]
