class Solution:

    def solution(self, t, nums):
        result = []
        self.backtracking(0, t, sorted(nums), result, [], 0)
        print(f"Numero di soluzioni trovate: {len(result)}")
        print(f"Soluzioni: {result}")

    def is_valid(self, somma_corrente, valore, t):
        return ((somma_corrente + valore) <= t)
    
    def is_a_solution(self, somma_corrente, t):
        return (somma_corrente == t)

    def backtracking(self, somma_corrente, t, nums, result, addendi, start):
        # Stampa per tracciare lo stato corrente
        print(f"\nChiamata a backtracking con: somma_corrente={somma_corrente}, addendi={addendi}, start={start}")
        
        if self.is_a_solution(somma_corrente, t):
            print(f"** Trovata una soluzione: {addendi}")
            if addendi not in result:
                result.append(addendi[:])
            return 
        else:
            for i in range(start, len(nums)):
                if self.is_valid(somma_corrente, nums[i], t):
                    print(f"--> Aggiungo {nums[i]} alla somma corrente {somma_corrente}")
                    somma_corrente += nums[i]
                    addendi.append(nums[i])

                    self.backtracking(somma_corrente, t, nums, result, addendi, i+1)

                    # Backtrack
                    print(f"<-- Rimuovo {nums[i]} dalla somma corrente {somma_corrente}")
                    somma_corrente -= nums[i]
                    addendi.pop()
                else:
                    print(f"Numero {nums[i]} non valido per la somma corrente {somma_corrente}. Esco dal ciclo.")
                    break


# Esempio di utilizzo
s = Solution()
nums = [4, 3, 2, 2, 1, 1]
s.solution(4, nums)

nums = [2, 1, 1]
s.solution(5, nums)

nums = [50,50,50,50,50,50,25,25,25,25,25,25]
s.solution(400,nums)