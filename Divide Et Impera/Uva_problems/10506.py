class Solution:

    def solution(self, M, N):
        s = []  # Sequenza da costruire
        checked = []  # Combinazioni di M numeri già verificate
        print(f"Avvio del backtracking con M={M} e N={N}")
        self.backtracking(N, M, s, checked)
        print("Sequenza finale:", s)

    def is_valid(self, M, N, s, checked):
        print(f"\nVerifica se la sequenza {s[-M:]} è valida...")
        if len(s) < (M**N):  # Non abbiamo ancora costruito la sequenza completa
            valid = (s[-M:] not in checked) or (len(s) < M)
            print(f"  La sequenza {s[-M:]} è {'valida' if valid else 'non valida'}")
            return valid
        elif len(s) == (M**N):  # Sequenza completa
            valid = ((s[-M:] not in checked) and ((s[-1:] + s[:M-1]) not in checked)) or (len(s) < M)
            print(f"  La sequenza finale {s[-M:]} è {'valida' if valid else 'non valida'}")
            return valid

    def is_finished(self, n, M, s):
        # Verifica se la sequenza è lunga abbastanza
        is_finished = len(s) == (M ** n)
        print(f"Verifica se la sequenza è completa: {is_finished}")
        return is_finished

    def construct_candidates(self, c, N):
        # Costruisce i candidati (i numeri da 0 a N-1)
        c = [i for i in range(N)]
        print(f"Costruiti i candidati: {c}")
        return c

    def backtracking(self, n, M, s, checked):
        print(f"\nAvvio del backtracking, sequenza parziale: {s}")
        
        if self.is_finished(n, M, s):
            print(f"Sequenza completa raggiunta: {s}")
            return True
        else:
            c = []
            c = self.construct_candidates(c, n)
            for elem in c:
                print(f"\nProvo ad aggiungere {elem} alla sequenza.")
                s.append(elem)
                
                # Verifica se la sequenza parziale è valida
                if self.is_valid(M, n, s, checked):
                    print(f"Sequenza valida: {s}")
                    
                    # Aggiungi alla lista checked se la sequenza ha almeno M cifre
                    if len(s) >= M:
                        checked.append(s[-M:])
                        print(f"Combinazione aggiunta a checked: {s[-M:]}")

                    # Chiamata ricorsiva
                    if self.backtracking(n, M, s, checked):
                        return True

                    # Se la ricorsione fallisce, rimuovo l'elemento e continuo a tentare
                    if len(s) >= M:
                        checked.remove(s[-M:])
                        print(f"Combinazione rimossa da checked: {s[-M:]}")
                s.pop()  # Rimuovo l'ultimo elemento per tentare un altro
                print(f"Rimosso {elem}, sequenza parziale: {s}")
            
            return False

if __name__ == "__main__":
    s = Solution()
    #s.solution(2, 3)  # Esempio: M=2, N=3
    #s.solution(4, 2)  # Esempio: M=2, N=3
    s.solution(3,3)