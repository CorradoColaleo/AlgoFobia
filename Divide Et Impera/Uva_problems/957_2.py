import math
class Solution:
    
    def solution(self, y, nums):
        print(f"Periodo considerato: {y} anni")
        print(f"Lista delle elezioni dei papi: {nums}")
        solution = self.divide_et_impera(y, nums, 0, len(nums) - 1)
        print(f"Risultato finale: Numero di Papi: {solution[0]}, Primo Papa: {solution[1]}, Ultimo Papa: {solution[2]}")

    def middle(self, y, nums, q, p, r):
        print(f"\nCalcolo middle per q={q}, p={p}, r={r}")
        if q + 1 > r or nums[q + 1] - nums[q] > y:
            print("Intervallo troppo piccolo o fuori limite")
            return 0, 0, 0

        bordo_sx = q
        bordo_dx = q + 1
        print(f"Inizializzazione: bordo_sx={bordo_sx}, bordo_dx={bordo_dx}")

        while (bordo_sx >= p and nums[q + 1] - nums[bordo_sx] < y):
            bordo_sx -= 1
        bordo_sx += 1
        print(f"Bordo sinistro trovato: bordo_sx={bordo_sx}")

        while (bordo_dx <= r and nums[bordo_dx] - nums[q] < y):
            bordo_dx += 1
        bordo_dx -= 1
        print(f"Bordo destro trovato: bordo_dx={bordo_dx}")

        massimo = 0
        first = 0
        last = 0
        for i in range(bordo_sx, q + 1):
            j = q + 1
            while j <= bordo_dx and nums[j] - nums[i] < y:
                j += 1
            j -= 1
            print(f"Controllo intervallo: i={i}, j={j}, numero di papi={j - i + 1}")

            if massimo < j - i + 1:
                massimo = j - i + 1
                first = nums[i]
                last = nums[j]
                print(f"Nuovo massimo trovato: massimo={massimo}, first={first}, last={last}")

        return massimo, first, last

    def merge(self, y, nums, q, p, r, int_sx, first_sx, last_sx, int_dx, first_dx, last_dx):
        print(f"\nMerge tra segmenti con q={q}, p={p}, r={r}")
        int_c, first_c, last_c = self.middle(y, nums, q, p, r)
        print(f"Confronto: sx={int_sx}, middle={int_c}, dx={int_dx}")
        
        massimo = max(int_sx, int_c, int_dx)
        if massimo == int_sx:
            print(f"Selezionato segmento sinistro: {int_sx}")
            return int_sx, first_sx, last_sx
        elif massimo == int_c:
            print(f"Selezionato segmento middle: {int_c}")
            return int_c, first_c, last_c
        else:
            print(f"Selezionato segmento destro: {int_dx}")
            return int_dx, first_dx, last_dx 

    def divide_et_impera(self, y, nums, p, r):
        print(f"\nDivide et impera per intervallo: p={p}, r={r}")
        if p == r:
            print(f"Intervallo di un solo elemento: anno {nums[p]}")
            return 1, nums[p], nums[r]
        
        q = math.floor((p + r) / 2)
        print(f"Divido a metà: q={q}")

        int_sx, first_sx, last_sx = self.divide_et_impera(y, nums, p, q)
        int_dx, first_dx, last_dx = self.divide_et_impera(y, nums, q + 1, r)
        int_result, first_result, last_result = self.merge(y, nums, q, p, r, int_sx, first_sx, last_sx, int_dx, first_dx, last_dx)

        print(f"Risultato combinato: massimo={int_result}, primo={first_result}, ultimo={last_result}")
        return int_result, first_result, last_result


if __name__ == "__main__":
    s = Solution()
    s.solution(5, [1, 2, 3, 6, 8, 12, 13, 13, 15, 16, 17, 18, 19, 20, 20, 21, 25, 26, 30, 31])
