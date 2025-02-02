class Solution:

    def longestNiceSubstring(self, s: str) -> str:

        if len(s)<=1:

            return ""

        index = -1

        for i in range(len(s)):

            if (s[i].islower and s[i].upper() not in s) or (s[i].isupper and s[i].lower()  not in s):

                index = i 

        if index==-1:

            return s

        else:
            
            r1 = self.longestNiceSubstring(s[0:index])

            r2 = self.longestNiceSubstring(s[index+1:len(s)])

            if (len(r1)>=len(r2)):

                return r1

            else:

                return r2




if __name__=="__main__":

    s = Solution()

    print(s.longestNiceSubstring("YazaAay"))







                

                




        