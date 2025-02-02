import math

def countingSortForRadix(A, B, exp, k):
    # A: array di input
    # B: array di output ordinato
    # exp: indica la cifra su cui ordinare (1 per unità, 10 per decine, ecc.)
    # k: il numero massimo di valori per le cifre (nel caso delle cifre da 0 a 9, k=9)

    C = [0] * (k + 1)

    # Conta le occorrenze delle cifre basate su exp (cifra corrente)
    for i in range(0, len(A)):
        index = (A[i] // exp) % 10  # Estrae la cifra corrispondente
        C[index] += 1

    print(f"[DEBUG] Stampa 1 del vettore C per exp={exp}: {C}")

    # Crea il conteggio cumulativo
    for j in range(1, k + 1):
        C[j] += C[j - 1]

    print(f"[DEBUG] Stampa 2 del vettore C per exp={exp}: {C}")

    # Costruisce l'array ordinato
    w = len(A) - 1
    while w >= 0:
        index = (A[w] // exp) % 10  # Estrae la cifra corrispondente
        B[C[index] - 1] = A[w]
        print(f"Ho messo {A[w]} in posizione {C[index]}")
        C[index] -= 1
        w -= 1

def radixSort(A):
    # Trova il numero massimo per sapere quante cifre considerare
    max_num = max(A)

    # Array di output (inizialmente vuoto)
    B = [0] * len(A)

    # Applica Counting Sort per ciascuna cifra (unità, decine, centinaia, ecc.)
    exp = 1
    while max_num // exp > 0:
        print(f"\n[DEBUG] Counting sort per exp={exp}")
        countingSortForRadix(A, B, exp, 9)  # 9 perché le cifre vanno da 0 a 9
        A[:] = B[:]  # Copia il contenuto ordinato di B in A per il prossimo ciclo
        print(f"[DEBUG] Array dopo exp={exp}: {A}")
        exp *= 10

if __name__ == "__main__":
    A = [329,457,657,839,436,720,355]
    print(f"Array originale: {A}")
    radixSort(A)
    print(f"Array ordinato: {A}")
