def minLength(s: str) -> int:
    
    stack = []

    # Iteriamo ogni carattere della stringa
    for char in s:
        # Se lo stack non è vuoto e i primi due caratteri formano "AB" o "CD", rimuoviamo
        if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
            stack.pop()  # rimuoviamo l'ultimo elemento dallo stack (es. A o C)
        else:
            # Aggiungiamo il carattere nello stack
            stack.append(char)

    # La lunghezza finale dello stack è la lunghezza minima ottenibile
    return len(stack)

# Esempi
s1 = "ABFCACDB"
print(minLength(s1))  # Output: 2

s2 = "ACBBD"
print(minLength(s2))  # Output: 5


