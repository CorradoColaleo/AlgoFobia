class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        
        def ricerca_posiz(lettera,chars):
            for i in range(len(chars)):
                if chars[i]==lettera:
                    return i 
        costi = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}
        n = len(s)
        dp = [float("-inf")] * n
        dp[-1]=costi[s[-1]] if (s[-1] not in chars) else vals[ricerca_posiz(s[-1],chars)]
        counter = max(0,dp[-1])
        for i in range(n-2,-1,-1):
            costo_i = costi[s[i]] if (s[i] not in chars) else vals[ricerca_posiz(s[i],chars)]
            dp[i] = max(costo_i,costo_i+dp[i+1])
            if dp[i] > counter:
                counter = dp[i]
        return counter