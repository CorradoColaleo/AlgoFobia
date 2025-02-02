import math

def insertionSort(v):

    if len(v)==1:

        return v

    for j in range(1,len(v)):
        
        key = v[j]

        i = j-1

        while i>=0 and v[i]>key:

            v[i+1]=v[i]

            i = i-1

        v[i+1]=key

    print(v)

    return v

def bucketSort(A):

    n = len(A)

    B = [[] for _ in range(n)]  # CORRETTO

    for i in range(n):

        B[math.floor(n*A[i])].append(A[i])

    print(f"[DEBUG] B non ordinato = {B}") 

    for j in range(n):

        insertionSort(B[j])

    print(f"[DEBUG] B ordinato = {B}")    

    C = []

    for w in range(n):

        C +=B[w]

    return C


if __name__=="__main__":

    A =[0.78,0.17,0.39,0.26,0.72,0.94,0.21,0.12,0.23,0.68]

    C = bucketSort(A)

    print(C)



