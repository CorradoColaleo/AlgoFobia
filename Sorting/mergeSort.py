import math

# Dichiaro la variabile globale counter
counter = 0

def mergeSort(A, p, r):
    print(f"mergeSort chiamato su A[{p}:{r}] -> {A[p:r+1]}")
    
    if p < r:
        q = (p + r) // 2  # Divisione intera in Python
        print(f"Divido A[{p}:{r}] in A[{p}:{q}] e A[{q+1}:{r}]")
        
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)
        
        print(f"Dopo merge: A[{p}:{r}] -> {A[p:r+1]}")  # Risultato parziale

def merge(A, p, q, r):
    global counter  # Dichiarazione per accedere alla variabile globale
    counter += 1  # Incremento del counter globale ad ogni chiamata di merge
    
    print(f"\nChiamata {counter} a merge: unisco A[{p}:{q}] ({A[p:q+1]}) con A[{q+1}:{r}] ({A[q+1:r+1]})")
    
    n1 = q - p + 1
    n2 = r - q
    
    # Crea array temporanei L e R
    L = A[p:q+1]  # L contiene A[p] fino ad A[q]
    R = A[q+1:r+1]  # R contiene A[q+1] fino ad A[r]
    
    # Aggiungi valori sentinella alla fine di L e R (9999999 è un numero molto grande)
    L.append(float('inf'))
    R.append(float('inf'))
    
    i = 0  # Indice iniziale di L
    j = 0  # Indice iniziale di R
    
    print(f"Array temporanei creati: L = {L[:-1]} (con sentinella), R = {R[:-1]} (con sentinella)")
    
    # Unisci le liste temporanee nell'array A[p..r]
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        
        print(f"Unisco in A[{k}]: {A[p:r+1]}")  # Stampa dopo ogni fusione parziale

if __name__ == "__main__":
    v = [7, 3, 6, 1, 2, 8]
    
    print("Array iniziale:", v)
    mergeSort(v, 0, len(v) - 1)  # Chiama mergeSort per ordinare l'array
    print("\nArray ordinato finale:", v)  # Stampa l'array ordinato
    print(f"\nNumero totale di chiamate a merge: {counter}")

