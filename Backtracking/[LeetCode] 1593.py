class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        result = []
        print(f"Inizio con la stringa: {s}")
        self.backtracking(0, 0, s, result, [])
        print(f"Risultato finale (numero massimo di sottostringhe uniche): {len(result)}")
        print(f"Sottostringhe finali: {result}")
        return len(result)
        
    def backtracking(self, index, step, s, result, current):

        flag = True

        print(f"\nChiamata a backtracking(index={index}, step={step}, current={current}, result={result})")
        
        # Condizione di fine
        if step == len(s):
            print(f" Fine della stringa raggiunta con current={current} e result={result}")
            if len("".join(current)) == len(s):
                if len(current) > len(result):
                    print(f" Nuovo risultato trovato! Aggiorno result con current={current}")
                    result[:] = current[:]  # Copio il contenuto di current in result
            return

        # Caso: sottostringa già vista
        if s[index:step+1] in current:
            print(f" Sottostringa '{s[index:step+1]}' già presente in current={current}, esco.")
            flag = False  
        else:
            # Aggiungo la nuova sottostringa
            print(f" Aggiungo la sottostringa '{s[index:step+1]}' a current={current}.")
            current.append(s[index:step+1])
        
        if flag:
            # Proseguo con la prossima suddivisione
            self.backtracking(step+1, step+1, s, result, current)

            # Rimuovo l'ultimo elemento aggiunto (backtracking)
            print(f" Rimuovo la sottostringa '{current[-1]}' da current per backtracking.")
            current.pop()

        # Provo senza aggiungere questa sottostringa
        print(f" Provo a continuare senza aggiungere '{s[index:step+1]}'.")
        self.backtracking(index, step+1, s, result, current)
        

if __name__ == "__main__":
    s = "ababccc"
    print(Solution().maxUniqueSplit(s))
