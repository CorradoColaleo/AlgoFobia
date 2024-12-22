class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*len(s)
        for i in range(len(s)-1,-1,-1):
            if len(s[i:])==1:
                if s[i:] in wordDict:
                    dp[i]=True
            else:
                for j in range(i,len(s)):
                    if j == len(s)-1:
                        if s[i:] in wordDict:
                            dp[i]=True
                            break
                    else:
                        if s[i:j+1] in wordDict and dp[j+1] is True:
                            dp[i]=True
                            break
        return dp[0]