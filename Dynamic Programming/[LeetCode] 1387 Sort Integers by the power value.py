class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(memo, x):
            if x == 1:
                memo[x] = 1 
                return 1
            if x in memo:
                return memo[x] + 1
            if (x % 2) == 0:
                value = x / 2
            else:
                value = (3 * x) + 1
            result = power(memo, value)
            memo[x] = result
            return result + 1

        memo = {}
        result = []
        for i in range(lo, hi + 1):
            power(memo, i)
            result.append((i, memo[i]))
        ordinata = sorted(result, key=lambda x: x[1])
        return ordinata[k - 1][0]
