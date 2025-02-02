def Partition(A,p,r):

    x = A[r]

    i = p-1

    for j in range(p,r):

        if A[j]<=x:

            i+=1

            (A[i],A[j]) = (A[j],A[i])

    (A[i+1],A[r]) = (A[r],A[i+1])

    return i+1

def quickSort(A,p,r):

    if p<r:

        q = Partition(A,p,r)

        quickSort(A,p,q-1)

        quickSort(A,q+1,r)
    

if __name__=="__main__":

    V = [2,1,3,8,7,5,6,4]

    quickSort(V,0,len(V)-1)

    print(V)

    