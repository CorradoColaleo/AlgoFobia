class Solution():
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = []
        self.backtracking(result,nums[:],nums,target,0)
        return len(result)
    
    def is_finished(self,step,nums):
        return (step==len(nums))

    def process_solution(self,current,result,target,nums,step):
        if (sum(current)==target):
            result.append(current[:])
    
    def backtracking(self,result,current,nums,target,step):
        if (self.is_finished(step,nums)):
            self.process_solution(current,result,target,nums,step)
            return
        self.backtracking(result,current,nums,target,step+1)
        current[step] = -current[step]
        self.backtracking(result,current,nums,target,step+1)
        current[step] = -current[step]




        