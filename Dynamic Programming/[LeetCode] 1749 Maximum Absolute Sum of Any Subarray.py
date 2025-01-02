class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        valorePiuPiccolo = nums[-1]
        valorePiuGrande = nums[-1]
        res = abs(nums[-1])
        for i in range(n-2,-1,-1):
            valorePiuPiccolo = min(nums[i],nums[i]+valorePiuPiccolo)
            valorePiuGrande = max(nums[i],nums[i]+valorePiuGrande)  
            res = max(abs(nums[i]),abs(valorePiuGrande),abs(valorePiuPiccolo),res)      
        return res