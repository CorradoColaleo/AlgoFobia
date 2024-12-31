def solution(S, profitti, pesi, n):
    if n == 0 or S == 0:
        return 0
    
    # Inizializziamo la tabella dp con (n+1) righe e (S+1) colonne
    dp = [[0] * (S + 1) for _ in range(n + 1)]
    
    # Iteriamo sugli oggetti al contrario (bottom-up)
    for oggetto in range(n - 1, -1, -1):
        for peso in range(S + 1):  # Peso residuo da 0 a S
            # Se il peso dell'oggetto corrente è minore o uguale al peso residuo
            if pesi[oggetto] <= peso:
                # Considera il massimo profitto tra includere o escludere l'oggetto
                dp[oggetto][peso] = max(
                    profitti[oggetto] + dp[oggetto + 1][peso - pesi[oggetto]],
                    dp[oggetto + 1][peso]
                )
            else:
                # Non possiamo includere l'oggetto corrente
                dp[oggetto][peso] = dp[oggetto + 1][peso]
    
    # Il massimo profitto sarà nella prima cella della tabella
    return dp[0][S]

S = 10
profitti = []
pesi = []
n = 0
print(solution(S, profitti, pesi, n))  # Output atteso: 0

S = 0
profitti = [10, 20, 30]
pesi = [1, 2, 3]
n = len(profitti)
print(solution(S, profitti, pesi, n))  # Output atteso: 0

S = 5
profitti = [10]
pesi = [3]
n = len(profitti)
print(solution(S, profitti, pesi, n))  # Output atteso: 10

S = 5
profitti = [10, 20, 30]
pesi = [3, 2, 4]
n = len(profitti)
print(solution(S, profitti, pesi, n))  # Output atteso: 30

S = 5
profitti = [10, 40, 30]
pesi = [3, 3, 3]
n = len(profitti)
print(solution(S, profitti, pesi, n))  # Output atteso: 40

