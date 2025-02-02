class Solution:

    def convert_B_to_D(self,matrix):
        #Caso base
        first_bit = matrix[0][0]
        done = True 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]!=first_bit:
                    done = False 
        if (done):
            return first_bit
        result = "D"
        #divide
        list_matrix = self.divide_matrix(matrix)
        # Impera
        for m in list_matrix:
            if m: 
                result += str(self.convert_B_to_D(m))
        return result

    def divide_matrix(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        # Se la matrice è vuota, restituisce None
        if rows == 0 or cols == 0:
            return None
        # Caso speciale per matrice 1xN o Nx1
        if rows == 1 and cols > 1:  # Matrice 1xN
            mid_col = (cols + 1) // 2
            return [matrix[0][:mid_col]], [matrix[0][mid_col:]], [], []
        if cols == 1 and rows > 1:  # Matrice Nx1
            mid_row = (rows + 1) // 2
            return [row[0] for row in matrix[:mid_row]], [], [row[0] for row in matrix[mid_row:]], []
        # Calcolo dei punti di divisione
        mid_row = (rows + 1) // 2  # Rigorosamente superiore per le righe dispari
        mid_col = (cols + 1) // 2  # Rigorosamente superiore per le colonne dispari
        # Creazione dei quadranti
        top_left = [row[:mid_col] for row in matrix[:mid_row]]
        top_right = [row[mid_col:] for row in matrix[:mid_row]]
        bottom_left = [row[:mid_col] for row in matrix[mid_row:]]
        bottom_right = [row[mid_col:] for row in matrix[mid_row:]]
        return top_left, top_right, bottom_left, bottom_right
        


if __name__=="__main__":

    matrix = [[0,0,1,0],[0,0,0,1],[1,0,1,1]]

    s = Solution()

    print(s.convert_B_to_D(matrix))