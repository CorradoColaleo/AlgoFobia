class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        if len(nums)==1:
            return True
        def solution(memo,nums):
            if tuple(nums) in memo:
                return memo[tuple(nums)]
            if len(nums)==2:
                memo[tuple(nums)]=max(nums[0],nums[1])
                return memo[tuple(nums)]
            result = max(nums[0]+(sum(nums[1:])-solution(memo,nums[1:])),nums[-1]+(sum(nums[:-1])-solution(memo,nums[:-1])))
            return result
        result = solution(memo,nums)
        if result >= sum(nums)-result:
            return True
        else:
            return False
    