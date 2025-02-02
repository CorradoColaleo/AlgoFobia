class Solution():

    @staticmethod
    def solution(mT,nT,L,rif,R,result):

        # L = (m,n), R = (m,n), rif = (m,n)

        if (mT==rif[0]) and (nT == rif[1]):

            return result

        if (Solution.fract(mT,nT) < Solution.fract(rif[0],rif[1])):

            result.append("L")

            return Solution.solution(mT,nT,L,Solution.costructor(L,rif),rif,result)

        else:

            result.append("R")

            return Solution.solution(mT,nT,rif,Solution.costructor(rif,R),R,result)

    def fract(m,n):

        if n==0:

            return 99999999

        return float(m/n)



    def costructor(L,R):

        return (L[0]+R[0],L[1]+R[1])

        

if __name__=="__main__":

    print(Solution.solution(5,7,(0,1),(1,1),(1,0),[]))

    print(Solution.solution(878,323,(0,1),(1,1),(1,0),[]))