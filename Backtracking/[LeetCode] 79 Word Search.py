"""1. is_finished: Devo fermarmi se ho superato la lunghezza della word target, se sono uscito fuori dalla matrice, se
la lettera non fa parte della parola target
2. is_a_solution: Devo avere una parola della stessa lunghezza della word target e devo vedere se effettivamente sono uguali
3. Logica del backtracking: In questo caso posso chiamare 4 volte il backtracking (sopra,sotto,destra,sinistra) ma devo mettere
un for fuori perchè la posizione iniziale chiaramente deve variare
*/ 
"""
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                self.visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                if (self.backtracking(board,word,"",i,j,len(board),len(board[0]),0)):
                    return True
        return False

    def is_finished(self,i,j,nrighe,ncolonne,currentWord,word,currentCharacter,board):
        if (i<0 or i>=nrighe) or (j<0 or j>=ncolonne):
            return True
        if (len(currentWord)==len(word)):
            return True
        if (self.visited[i][j]):
            return True
        if (word[currentCharacter] != board[i][j]):
            return True
    
    def is_solution(self,currentWord,word):
        if (len(currentWord)!=len(word)):
            return False
        else:
            if (currentWord == word):
                return True
            else:
                return False
    
    def backtracking(self,board,word,currentWord,i,j,nrighe,ncolonne,currentCharacter):
        result = False
        if (self.is_finished(i,j,nrighe,ncolonne,currentWord,word,currentCharacter,board)):
            if (self.is_solution(currentWord,word)):
                return True
            else:
                return False
        else:
            self.visited[i][j] = True
            currentWord+=str(board[i][j])
            result = self.backtracking(board,word,currentWord,i,j+1,nrighe,ncolonne,currentCharacter+1)
            if (result):
                return True
            result = self.backtracking(board,word,currentWord,i,j-1,nrighe,ncolonne,currentCharacter+1)
            if (result):
                return True
            result = self.backtracking(board,word,currentWord,i+1,j,nrighe,ncolonne,currentCharacter+1)
            if (result):
                return True
            result = self.backtracking(board,word,currentWord,i-1,j,nrighe,ncolonne,currentCharacter+1)
            if (result):
                return True
            self.visited[i][j] = False
            currentWord = currentWord[:-1]
        return result


if __name__ == "__main__":
    # Creazione di un'istanza della soluzione
    solution = Solution()
    
    # Definizione della matrice e della parola da cercare
    board = [
        ["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]
    ]
    word = "SEE"

    # Verifica se la parola esiste nella matrice
    exists = solution.exist(board, word)
    
    # Stampa il risultato
    print(f"La parola '{word}' esiste nella matrice: {exists}")


        
        