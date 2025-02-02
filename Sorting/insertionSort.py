#Algoritmo di insertion sort

def insertionSort(v):

    if len(v)==1:

        return v

    for j in range(1,len(v)):
        
        key = v[j]

        i = j-1

        while i>=0 and v[i]>key:

            v[i+1]=v[i]

            i = i-1

            print(v)

        v[i+1]=key

    return v

if __name__=="__main__":

    vectorTesting = [2,5,9,3,4,1,10]

    print(insertionSort(vectorTesting))
