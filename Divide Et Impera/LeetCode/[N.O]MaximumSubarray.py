def MaximumSybarray(A,nA,nS):

    result = -9999999

    maxSubstring = None

    result2 = 0

    if nS==nA:

        result = sum(A)

        maxSubstring = A

    elif nS > nA:

        print("nS non può essere maggiore di nA")

        return -999999

    elif nS<nA and nS>=1:

        i = 0

        while (i+nS) <= len(A):

            r = sum(A[i:nS+i])

            if result<r:

                result = r

                maxSubstring = A[i:nS+i]

            i+=1

    if nS>=1:

        result2, substring = MaximumSybarray(A,nA,nS-1)

        if result >= result2:

            return result, maxSubstring

        else:

            return result2, substring

    else:

        return result, None

        
L = [-2,1,-3,4,-1,2,1,-5,4]

L2 = [1]

L3 = [5,4,-1,7,8]

print(MaximumSybarray(L,len(L),len(L)))

print(MaximumSybarray(L2,len(L2),len(L2)))

print(MaximumSybarray(L3,len(L3),len(L3)))
    

        
    

    



        

