class Solution:
    def solution(self,n):
        nums = []
        for i in range(1,n+1):
            nums.append(i)
        result = []
        dizionario_n_primi = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        self.backtracking(result,[1],nums,n,dizionario_n_primi)
        return result
        
    def is_finished(self,current,n):
        return (len(current)==n)

    def is_valid(self,current,dizionario_n_primi,n):
        if (len(current)==1):
            return True
        else:
            if (len(current)==n):
                return (((current[-1]+current[-2]) in dizionario_n_primi) and 
                ((current[0]+current[-1]) in dizionario_n_primi))
            else:
                return ((current[-1]+current[-2]) in dizionario_n_primi)
    
    def construct_candidates(self,c,current,nums):
        used = [False] * len(nums)
        for i in range(len(nums)):
            if nums[i] in current:
                used[i] = True
        for i in range(len(used)):
            if used[i] == False:
                c.append(nums[i])
    
    def backtracking(self,result,current,nums,n,dizionario_n_primi):
        if (not self.is_valid(current,dizionario_n_primi,n)):
            return
        if (self.is_finished(current,n)):
            result.append(current[:])
            return
        c = []
        self.construct_candidates(c,current,nums)
        for elem in c:
            current.append(elem)
            self.backtracking(result,current,nums,n,dizionario_n_primi)
            current.pop()

if __name__ == '__main__':
    n = int(input("Inserisci n: "))
    s = Solution()
    risultato = s.solution(n)
    print(risultato)