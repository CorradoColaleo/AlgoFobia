def solution(s1, s2=None, dp=None, i=None, j=None):
    # Inizializzo s2 come il reverse di s1 e dp come una tabella di memoization
    if s2 is None:
        s2 = s1[::-1]
    n = len(s1)
    if dp is None:
        dp = [[float("-inf")] * n for _ in range(n)]

    # Inizializzo i e j come indici massimi
    if i is None:
        i = len(s1) - 1
    if j is None:
        j = len(s2) - 1

    # Caso base: indici fuori dai limiti
    if i < 0 or j < 0:
        return 0

    # Memoization: restituisco il risultato già calcolato
    if dp[i][j] != float("-inf"):
        return dp[i][j]

    # Codice operativo
    if s1[i] == s2[j]:
        dp[i][j] = 1 + solution(s1, s2, dp, i - 1, j - 1)
    else:
        dp[i][j] = max(solution(s1, s2, dp, i, j - 1), solution(s1, s2, dp, i - 1, j))

    return dp[i][j]


# Test dei casi forniti
s1 = "adam"
print(solution(s1))  # Output: 3

s2 = "madam"
print(solution(s2))  # Output: 5

s3 = "mamdm"
print(solution(s3))  # Output: 5

s4 = "cde"
print(solution(s4))  # Output: 1
