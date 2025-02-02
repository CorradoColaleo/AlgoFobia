import math
def solution(A,p,r,k):

    if p==r:

        if A[p] < k:

            return (A[p],"x")

        elif A[p] > k:

            return ("x",A[p])

        else:

            return ("x","x")

    q = math.floor((p+r)/2)

    r1 = solution(A,p,q,k)
    
    r2 = solution(A,q+1,r,k)

    #Merge

    x1 = 0

    x2 = 0

    if r1[0] == "x":

        x1 = r2[0]

    elif r2[0] == "x":

        x1 = r1[0]

    else:

        x1 = max(r1[0],r2[0])

    if r1[1] == "x":

        x2 = r2[1]

    elif r2[1] == "x":

        x2 = r1[1]

    else:

        x2 = min(r1[1],r2[1])

    return x1,x2


A = [1,4,5,7]


print(solution(A,0,len(A)-1,4))

print(solution(A,0,len(A)-1,6))

print(solution(A,0,len(A)-1,8))

print(solution(A,0,len(A)-1,10))
