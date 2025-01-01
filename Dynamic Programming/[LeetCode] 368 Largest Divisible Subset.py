class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        if len(nums) == 2:
            return nums if ((nums[0] % nums[1] == 0) or (nums[1] % nums[0] == 0)) else [min(nums)]
        nums.sort()
        dp = [1] * len(nums)  # Ogni elemento forma almeno un sottoinsieme di lunghezza 1
        prev = [-1] * len(nums)  # Array per tracciare gli indici precedenti nella sequenza
        max_index = 0  # Indice del massimo valore di dp

        # Calcolo del dp senza usare il flag "first"
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if (nums[j] % nums[i] == 0) or (nums[i] % nums[j] == 0):
                    if dp[i] < 1 + dp[j]:
                        dp[i] = 1 + dp[j]
                        prev[i] = j
            if dp[i] > dp[max_index]:
                max_index = i

        # Ricostruzione della sequenza
        result = []
        current = max_index
        while current != -1:
            result.append(nums[current])
            current = prev[current]

        # Restituisce il risultato
        return result
