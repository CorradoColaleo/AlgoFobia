class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        
        def solution(l, r):
            if l > r:
                return 0  # Caso base: nessun palloncino tra l e r
            
            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                # Calcola il numero di monete per scoppiare il palloncino i
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += solution(l, i - 1) + solution(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            
            return dp[(l, r)]
        
        return solution(1, len(nums) - 2)
