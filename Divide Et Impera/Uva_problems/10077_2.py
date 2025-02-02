class Solution:

    def solution(self,target,A,result):
        if (target==A[1]):
            return result
        elif (self.fract(target[0],target[1]) < self.fract(A[1][0],A[1][1])):
            result.append("L")
            A = [A[0],(A[0][0]+A[1][0],A[0][1]+A[1][1]),A[1]]
            return self.solution(target,A,result)
        else:
            result.append("R")
            A = [A[1],(A[1][0]+A[2][0],A[1][1]+A[2][1]),A[2]]
            return self.solution(target,A,result)
    
    def fract(self,num,den):
        return float(num/den)


A = [(0,1),(1,1),(1,0)]
s = Solution()
print(s.solution((5,7),A,[]))
print(s.solution((878,323),A,[]))
