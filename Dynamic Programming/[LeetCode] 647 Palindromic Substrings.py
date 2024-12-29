class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            #Copro le sequenze palindrome di lunghezza dispari
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            
            #Copro le sequenze palindrome di lunghezza pari
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
        return res