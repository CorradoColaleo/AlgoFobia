class Solution:
    def grayCode(self, n: int) -> list[int]:
        result = [0]
        print(f"Inizio generazione Gray Code per n = {n}")
        self.backtracking(result, n)
        print(f"Risultato finale: {result}")
        return result

    def is_finished(self, current, n):
        print(f"Verifica se la lunghezza è sufficiente: {len(current)} su {2**n}")
        return (len(current) == (2**n))

    def different_bit(self, str1, str2):
        different = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                different += 1
        print(f"Differenza tra {str1} e {str2}: {different} bit differenti")
        return different

    def is_a_solution(self, current, n):
        print(f"Verifica se {current} è una soluzione valida")
        binary_current = []
        for elemento in current:
            binary_current.append(format(elemento, f'0{n}b'))
        print(f"Rappresentazione binaria: {binary_current}")
        diff1 = self.different_bit(binary_current[0], binary_current[len(binary_current) - 1])
        if diff1 > 1:
            print("Fallito al primo check (primo e ultimo bit)")
            return False
        for i in range(len(binary_current) - 1):
            if (self.different_bit(binary_current[i], binary_current[i + 1]) > 1):
                print(f"Fallito al check tra {binary_current[i]} e {binary_current[i + 1]}")
                return False
        print("Trovata soluzione valida")
        return True

    def construct_candidates(self, c, current, n):
        print(f"Costruzione candidati per {current}")
        for i in range(1, (2**n)):
            if i not in current:
                c.append(i)
        print(f"Candidati trovati: {c}")

    def backtracking(self, current, n):
        print(f"Backtracking con corrente = {current}")
        if self.is_finished(current, n):
            print(f"Lunghezza raggiunta con {current}, verifica soluzione")
            if self.is_a_solution(current, n):
                return current
            else:
                return -1
        c = []
        self.construct_candidates(c, current, n)
        for candidato in c:
            print(f"Aggiungo candidato {candidato}")
            current.append(candidato)
            result = self.backtracking(current, n)
            if result != -1:
                return result
            print(f"Rimuovo candidato {candidato}")
            current.pop()
        return -1


s = Solution()
s.grayCode(4)
