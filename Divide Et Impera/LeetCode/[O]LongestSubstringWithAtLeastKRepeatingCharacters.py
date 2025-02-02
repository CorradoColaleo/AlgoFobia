class Solution:

    def longestSubstring(self, s: str, k: int) -> int:
        
        # Caso base

        dizionario = {}

        for i in range(len(s)):

            try:

                dizionario[s[i]]=0

            except:

                pass

        for character in s:

            dizionario[character]+=1

        done = False

        finalKey = None

        for chiave in dizionario.keys():

            if dizionario[chiave]<k:

                done = True

                if finalKey == None:

                    finalKey = chiave

                    print(finalKey)

        if done == False:
            
            return len(s)

        else:

            index = 0

            for i in range(len(s)):

                if s[i]==finalKey:

                    index = i

                    print(index)

            print(f"Confrontro tra {s[0:index]} e {s[index+1:len(s)]}")

            r1 = self.longestSubstring(s[0:index],k)

            r2 = self.longestSubstring(s[index+1:len(s)],k)

            if r1>=r2:

                return r1

            else:

                return r2

if __name__=="__main__":

    s = Solution()

    print(s.longestSubstring("bbaaacbd",3))
    




