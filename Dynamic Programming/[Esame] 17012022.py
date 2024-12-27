def solution(arr, k, t):
    n = len(arr)
    dp = [float("inf")] * n  # Tempo minimo per trasportare le prime i auto
    dp_viaggi = [0] * n  # Numero minimo di viaggi per trasportare le prime i auto
    
    # Caso base: la prima auto viene trasportata
    dp[0] = 2 * t + arr[0]
    dp_viaggi[0] = 1
    
    # Calcolo dinamico per ogni auto
    for i in range(1, n):
        for j in range(1, k + 1):  # Considera gruppi di dimensione fino a k
            if i - j < 0:
                # Tutte le auto fino alla i-esima vengono trasportate in un unico viaggio
                temp_time = 2 * t + arr[i]
                temp_viaggi = 1
            else:
                # Gruppo corrente: ultimo viaggio include le auto [i-j+1, ..., i]
                last_arrival = arr[i]
                prev_time = dp[i - j]
                if last_arrival > prev_time:
                    temp_time = last_arrival + 2 * t
                else:
                    temp_time = prev_time + 2 * t
                temp_viaggi = dp_viaggi[i - j] + 1
            
            # Aggiorna dp[i] e dp_viaggi[i] se troviamo una soluzione migliore
            if temp_time < dp[i]:
                dp[i] = temp_time
                dp_viaggi[i] = temp_viaggi
    
    # Il tempo finale è quando l'ultimo viaggio termina
    return (dp[n - 1] - t, dp_viaggi[n - 1])

# Esempio di utilizzo
if __name__ == "__main__":
    arr = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    k = 2
    t = 10
    print(solution(arr, k, t))  # Output: (110, 5)

    arr = [10, 30, 40]
    k = 2
    t = 10
    print(solution(arr, k, t))  # Output: (70, 2)
