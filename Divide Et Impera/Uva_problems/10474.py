class Solution:
    def solution(self,A,target):
        A = sorted(A)
        print(A)
        print(self.divide_et_impera(A,0,len(A)-1,target))
    def divide_et_impera(self,A,p,r,target):
        if (p==r):
            if (A[p]==target):
                return f"{A[p]} found at {p+1}"
            else:
                return f"{target} not found"
        q = (p+r)//2
        if ((A[q] == target) and (q==0)):
            return f"{A[q]} found at {q+1}"
        if ((A[q] == target) and (A[q-1]!=target)):
            return f"{A[q]} found at {q+1}"
        else:
            if (A[q]>=target):
                return self.divide_et_impera(A,p,q-1,target)
            else:
                return self.divide_et_impera(A,q+1,r,target)

if __name__ == "__main__":
    s = Solution()
    s.solution([2,3,5,1],5)
    s.solution([1,3,3,3,3,1],2)
    s.solution([1,3,3,3,3,1],3)