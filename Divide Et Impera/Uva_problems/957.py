import math

class Solution1:

    def Solution(self, A, Y, p, r):
        # Caso base: se p > r, non ci sono papi in questo intervallo
        if p > r:
            return 0, 0, 0

        q = math.floor((p + r) / 2)  # Indice centrale
        first = A[q]  # Anno del papa centrale
        last = 0
        npopes = 1
        i = q
        counter = 0

        # Stampa per debug: anno centrale
        print(f"Analizzando la metà con q = {q}, anno = {A[q]}")

        # Conta il numero di papi nell'intervallo di Y anni
        while i < len(A) and A[i] <= (A[q] + (Y - 1)):
            counter += 1
            last = A[i]
            i += 1

        npopes = counter  # Numero totale di papi trovati
        print(f"Numero di papi trovati nell'intervallo: {npopes}, da {first} a {last}")

        if p < r:
            npopesMax = 0
            firstMax = 0
            lastMax = 0

            # Ricorsione nella metà sinistra
            npopes1, first1, last1 = self.Solution(A, Y, p, q - 1)
            print(f"Risultato dalla metà sinistra: {npopes1}, {first1}, {last1}")

            # Ricorsione nella metà destra
            npopes2, first2, last2 = self.Solution(A, Y, q + 1, r)
            print(f"Risultato dalla metà destra: {npopes2}, {first2}, {last2}")

            # Confronto tra le due metà
            if npopes1 > npopes2:
                npopesMax = npopes1
                firstMax = first1
                lastMax = last1
                print("Maggiore nella metà sinistra.")
            elif npopes1 < npopes2:
                npopesMax = npopes2
                firstMax = first2
                lastMax = last2
                print("Maggiore nella metà destra.")
            else:
                if first1 <= first2:
                    npopesMax = npopes1
                    firstMax = first1
                    lastMax = last1
                    print("Pareggio, scelgo la metà sinistra.")
                else:
                    npopesMax = npopes2
                    firstMax = first2
                    lastMax = last2
                    print("Pareggio, scelgo la metà destra.")

            # Confronto finale per il massimo
            if npopesMax > npopes:
                print(f"Restituisco da metà: {npopesMax}, {firstMax}, {lastMax}")
                return npopesMax, firstMax, lastMax
            elif npopesMax < npopes:
                print(f"Restituisco dal centro: {npopes}, {first}, {last}")
                return npopes, first, last
            else:
                if firstMax < first:
                    print(f"Restituisco da metà (preferisco): {npopesMax}, {firstMax}, {lastMax}")
                    return npopesMax, firstMax, lastMax
                else:
                    print(f"Restituisco dal centro (preferisco): {npopes}, {first}, {last}")
                    return npopes, first, last

        return npopes, first, last


if __name__ == "__main__":

    s = Solution1()

    A = [1, 2, 3, 6, 8, 12, 13, 13, 15, 16, 17, 18, 19, 20, 20, 21, 25, 26, 30, 31]

    n, f, l = s.Solution(A, 5, 0, len(A) - 1)

    print("Final result: n =", n, "f =", f, "l =", l)

    print("-------------------------------------------")

    # Caso 1: Lista di anni consecutivi con Y diverso
    A1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n1, f1, l1 = s.Solution(A1, 5, 0, len(A1) - 1)
    print("Test case 1: n =", n1, "f =", f1, "l =", l1)

    print("-------------------------------------------")


    # Caso 2: Lista con intervalli maggiori tra anni
    A2 = [1, 10, 20, 30, 40, 50, 60]
    n2, f2, l2 = s.Solution(A2, 20, 0, len(A2) - 1)
    print("Test case 2: n =", n2, "f =", f2, "l =", l2)
    print("-------------------------------------------")

    # Caso 3: Lista con alcuni anni ripetuti
    A3 = [1, 5, 5, 10, 15, 15, 20, 25, 25]
    n3, f3, l3 = s.Solution(A3, 10, 0, len(A3) - 1)
    print("Test case 3: n =", n3, "f =", f3, "l =", l3)
    print("-------------------------------------------")

    # Caso 4: Lista con un singolo anno
    A4 = [100]
    n4, f4, l4 = s.Solution(A4, 5, 0, len(A4) - 1)
    print("Test case 4: n =", n4, "f =", f4, "l =", l4)
    print("-------------------------------------------")

    # Caso 5: Lista molto lunga per testare le prestazioni
    A5 = list(range(1, 1001, 10))  # Popes eletti ogni 10 anni
    n5, f5, l5 = s.Solution(A5, 100, 0, len(A5) - 1)
    print("Test case 5: n =", n5, "f =", f5, "l =", l5)
    print("-------------------------------------------")
