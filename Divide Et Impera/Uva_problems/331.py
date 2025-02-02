class Solution:
    def solution(self,nums,dataset):
        result = []
        self.backtracking(result,[],((len(nums)*((len(nums)-1)/2))),sorted(nums),nums)
        print(f"There are {len(result)} swap maps for input data set {dataset}")
        print(result)

    def is_finished(self,result,limite,sorted_vector,current,nums):
        if (nums == sorted_vector):
            if current != []:
                result.append(current[:])
            return True
        if (len(current)>=limite):
            return True
        return False

    def backtracking(self,result,current,limite,sorted_vector,nums):
        if (self.is_finished(result,limite,sorted_vector,current,nums)):
            return 
        for i in range(1,len(sorted_vector)):
            current.append(i)
            last_nums = nums[:]
            temp = nums[i]
            nums[i]=nums[i-1]
            nums[i-1]=temp 
            self.backtracking(result,current,limite,sorted_vector,nums)
            nums = last_nums[:]
            current.pop()

if __name__=="__main__":

    s = Solution()
    s.solution([9,7],1)
    s.solution([12,50],2)
    s.solution([3,2,1],3)
    s.solution([9,1,5],4)