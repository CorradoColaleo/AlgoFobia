import math

class Solution:

    def sieve(self,limit):

        # Algoritmo di Eratostene per trovare i numeri primi

        primes = [True] * (limit + 1)

        primes[0] = primes[1] = False

        for i in range(2, int(limit**0.5) + 1):

            if primes[i]:

                for j in range(i*i, limit + 1, i):

                    primes[j] = False

        return [i for i in range(2, limit + 1) if primes[i]]

    def GoldbachConjecture(self,n):

        lista_primi = self.sieve(int(math.pow(2,15)))

        result = 0

        for p1 in lista_primi:

            if p1 > n//2:

                break

            if (n-p1) in lista_primi:

                result+=1
        
        print(result)

        return result


if __name__=="__main__":

    s = Solution()

    s.GoldbachConjecture(10)
