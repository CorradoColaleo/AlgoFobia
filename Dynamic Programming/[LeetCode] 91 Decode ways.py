class Solution:
    def numDecodings(self, s: str) -> int:
        checklist = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
                     "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
                     "20", "21", "22", "23", "24", "25", "26"]

        n = len(s)
        if n == 0:  # Caso base: stringa vuota
            return 0

        dp = [0] * n  # Array per la programmazione dinamica

        # Caso con una sola cifra
        if n == 1:
            if s in checklist:
                return 1
            else:
                return 0

        # Controllo per l'ultimo carattere
        if s[-1] in checklist:
            dp[-1] = 1

        # Controllo per il penultimo carattere
        if s[-2] in checklist:
            if s[-2] + s[-1] in checklist:
                dp[-2] = 1 + dp[-1]
            else:
                dp[-2] = dp[-1]

        # Iterazione dal terzultimo carattere fino al primo
        for i in range(n - 3, -1, -1):
            if s[i] == "0":  # Uno '0' da solo non è valido
                dp[i] = 0
            else:
                # Somma delle possibilità da `i+1` (singolo carattere) e `i+2` (doppio carattere)
                dp[i] = dp[i + 1]
                if s[i] + s[i + 1] in checklist:
                    dp[i] += dp[i + 2]

        return dp[0]
