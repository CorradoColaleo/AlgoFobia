class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        print(nums)
        counter = 0
        
        # Funzione per contare le coppie che soddisfano una certa somma massima
        def countPairsWithSumLessThanOrEqualTo(target):
            count = 0
            left, right = 0, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] <= target:
                    count += (right - left)
                    left += 1
                else:
                    right -= 1
            return count

        # Conta coppie con somma <= upper
        totalPairsUpToUpper = countPairsWithSumLessThanOrEqualTo(upper)
        
        # Conta coppie con somma < lower (quindi da sottrarre)
        totalPairsBelowLower = countPairsWithSumLessThanOrEqualTo(lower - 1)
        
        # Il risultato finale è la differenza tra i due conteggi
        counter = totalPairsUpToUpper - totalPairsBelowLower
        
        print(counter)
        return counter

# Esempio di utilizzo
if __name__ == "__main__":
    s = Solution()
    nums = [1, 7, 9, 2, 5]
    s.countFairPairs(nums, 11, 11)
