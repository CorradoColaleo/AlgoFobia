def countingSort(A,B,k):

    C = [0] * (k+1)

    for i in range(0,len(A)):

        C[A[i]]+=1

    print(f"[DEBUG] Stampa 1 del vettore C: {C}")

    for j in range(1,k+1):

        C[j] += C[j-1]

    print(f"[DEBUG] Stampa 2 del vettore C: {C}")

    w = len(A)-1

    while w >= 0:

        B[C[A[w]]-1] = A[w]
        
        print(f"Ho messo {A[w]} in {C[A[w]]}")

        C[A[w]] -=1

        w -=1


if __name__=="__main__":

    A = [2,5,3,0,2,3,0,3]

    B = [0,0,0,0,0,0,0,0]

    countingSort(A,B,5)

    print(B)