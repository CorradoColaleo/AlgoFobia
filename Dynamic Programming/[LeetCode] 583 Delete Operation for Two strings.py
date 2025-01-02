class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        s1 = len(word1)
        s2= len(word2)
        dp=[[0]*(s2+1) for _ in range(s1+1)]
        dp[-1][-1]=0
        for colonna in range(s2+1):
            dp[-1][colonna]= s2-colonna
        for riga in range(s1+1):
            dp[riga][-1]=s1-riga
        for i in range(s1-1,-1,-1):
            for j in range(s2-1,-1,-1):
                dp[i][j]=(1+min(dp[i][j+1],dp[i+1][j])) if word1[i]!=word2[j] else dp[i+1][j+1]
        return dp[0][0]