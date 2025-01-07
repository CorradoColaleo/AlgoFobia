class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #Creo la matrice e la inizializzo con valori infiniti
        memo = [[float("inf")] * (len(word2)+1) for i in range(len(word1)+1)]
        
        #Riempio l'ultima riga (word1 vuota)
        for j in range(len(word2)+1):
            memo[len(word1)][j] = len(word2)-j
        
        #Riempio l'ultima colonna (word2 vuota)
        for i in range(len(word1)+1):
            memo[i][len(word2)] = len(word1)-i

        #riempio la matrice dalla fine all'inizio 
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    memo[i][j] = memo[i+1][j+1]
                else:
                    memo[i][j] = 1 + min(memo[i+1][j],memo[i][j+1],memo[i+1][j+1])
        return memo[0][0]
