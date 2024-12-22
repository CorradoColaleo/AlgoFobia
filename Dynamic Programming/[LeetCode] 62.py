class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Crea la griglia iniziale piena di zeri
        grid = [[0 for _ in range(n)] for _ in range(m)]
        print(f"Griglia iniziale ({m}x{n}):")
        for row in grid:
            print(row)
        print("\nCalcolo dei percorsi univoci...")
        
        result = self.dp(grid, 0, 0, m - 1, n - 1)  # Le coordinate finali sono m-1, n-1
        print("\nGriglia finale con i percorsi calcolati:")
        for row in grid:
            print(row)
        
        return result
        
    def dp(self, grid, i, j, m, n):
        # Stampa lo stato corrente
        print(f"Sto visitando la cella ({i}, {j})")

        # Caso base: raggiunta la cella in basso a destra
        if i == m and j == n:
            print(f" Raggiunto il punto finale ({i}, {j}). Imposto grid[{i}][{j}] = 1")
            grid[i][j] = 1
            return 1

        # Caso: bordo inferiore
        if j == n:
            print(f" Sul bordo destro ({i}, {j}). Controllo la cella sottostante.")
            if grid[i + 1][j] != 0:
                grid[i][j] = grid[i + 1][j]
            else:
                grid[i][j] = self.dp(grid, i + 1, j, m, n)
            return grid[i][j]

        # Caso: bordo destro
        if i == m:
            print(f" Sul bordo inferiore ({i}, {j}). Controllo la cella a destra.")
            if grid[i][j + 1] != 0:
                grid[i][j] = grid[i][j + 1]
            else:
                grid[i][j] = self.dp(grid, i, j + 1, m, n)
            return grid[i][j]

        # Caso generale: sommo i percorsi da destra e sotto
        print(f" Interno ({i}, {j}). Controllo destra e sotto.")
        if grid[i][j + 1] != 0 and grid[i + 1][j] != 0:
            grid[i][j] = grid[i + 1][j] + grid[i][j + 1]
        elif grid[i][j + 1] != 0 and grid[i + 1][j] == 0:
            grid[i][j] = self.dp(grid, i + 1, j, m, n) + grid[i][j + 1]
        elif grid[i][j + 1] == 0 and grid[i + 1][j] != 0:
            grid[i][j] = grid[i + 1][j] + self.dp(grid, i, j + 1, m, n)
        else:
            grid[i][j] = self.dp(grid, i + 1, j, m, n) + self.dp(grid, i, j + 1, m, n)
        
        print(f" Calcolato grid[{i}][{j}] = {grid[i][j]}")
        return grid[i][j]


# Main per testare la funzione
if __name__ == "__main__":
    m, n = 3,7  # Dimensioni della griglia
    print(f"Numero di percorsi univoci per una griglia {m}x{n}: {Solution().uniquePaths(m, n)}")
