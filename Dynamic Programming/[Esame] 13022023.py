def trova_min(cuts, C):
    # Inizializzazione della tabella DP
    DP = [[0] * (cuts + 1) for _ in range(cuts + 1)]

    # Iterazione per lunghezze crescenti dei segmenti
    for length in range(2, cuts + 1):  # Segmenti di lunghezza 2 in poi
        for i in range(cuts - length + 1):  # Tutti gli inizi possibili i
            j = i + length
            DP[i][j] = float('inf')
            for k in range(i + 1, j):  # I possibili tagli k
                DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j] + (C[j] - C[i]))
    return DP[0][cuts]

# Esempio di utilizzo:
# cuts = numero di tagli + 1 (includendo gli estremi)
# C = lista delle posizioni di taglio, inclusi 0 e n agli estremi

# Esempio basato sul codice
C = [0, 2, 20, 25, 30]
cuts = len(C) - 1  # Numero di tagli + 1 (inclusi gli estremi)
soluzione = trova_min(cuts, C)
print(f"Il costo minimo totale è: {soluzione}")
