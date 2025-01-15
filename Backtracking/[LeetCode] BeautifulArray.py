class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        nums=[]
        for i in range(1,n+1):
            nums.append(i)
        return self.backtracking(nums,[],n)
    
    def is_finished(self,current,n):
        return (len(current)==n)

    def is_a_solution(self,current):
        for i in range(len(current)):
            if (0<i<(len(current)-1)):
                for indice1 in range(0,i):
                    for indice2 in range(i+1,len(current)):
                        if (2*current[i]) == (current[indice1]+current[indice2]):
                            return False
        return True

    def construct_candidates(self,c,current,nums):
        used = [False] * len(nums)
        for i in range(len(nums)):
            if nums[i] in current:
                used[i] = True
        for i in range(len(used)):
            if used[i] == False:
                c.append(nums[i])
    
    def backtracking(self,nums,current,n):
        if (self.is_finished(current,n)):
            if (self.is_a_solution(current)):
                return current
            else:
                return -1
        else:
            c = []
            self.construct_candidates(c,current,nums)
            for elem in c:
                current.append(elem)
                if (self.backtracking(nums,current,n)!=-1):
                    return current
                else:
                    current.pop()
            return -1