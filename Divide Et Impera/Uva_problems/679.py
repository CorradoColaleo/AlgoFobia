class Solution:

    def solution(self,A,p,r):

        if ((p*2)+1)<r:

            if A[p][1] == False:

                A[p][1] = True

                return self.solutionConD4EUnaPallina(A,(2*p)+1,r)

            else:

                A[p][1] = False

                return self.solutionConD4EUnaPallina(A,(2*p)+2,r)

        else:

            return A[p][0],A


def main(D,I):

    L = []

    for i in range(0,pow(2,D)-1):

        L.append([i+1,False])

    soluzione = Solution()

    s = 0

    for i in range(I):
        
        s=soluzione.solution(L,0,len(L)-1)

    print(s[0])


if __name__=="__main__":

    main(4,2)
    main(3,4)
    main(10,1)
    main(2,2)
    main(8,128)
    