class Solution:
    def stoneGame(self, piles):
        punti = {}
        puntiPlayer1 = self.solution(tuple(piles), punti)  # Convertiamo `piles` in una tupla
        if puntiPlayer1 > sum(piles) - puntiPlayer1:
            return True
        else:
            return False

    def solution(self, piles, punti):
        if piles in punti:  # Ora `piles` è una tupla e può essere una chiave del dizionario
            return punti[piles]
        
        if len(piles) == 1:  # Caso base: solo una pila rimasta
            return piles[0]
        
        puntiTotali = sum(piles)
        puntiPlayer = puntiTotali - min(
            self.solution(piles[1:], punti),
            self.solution(piles[:-1], punti)
        )
        
        punti[piles] = puntiPlayer
        return punti[piles]
