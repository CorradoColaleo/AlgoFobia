class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Variabili per gestire la finestra scorrevole
        left = 0
        zero_count = 0
        max_length = 0

        # Itera attraverso l'array
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # Se ci sono più di 1 zero nella finestra, sposta il puntatore sinistro
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Calcola la lunghezza massima della finestra, escludendo un elemento
            max_length = max(max_length, right - left)

        return max_length
