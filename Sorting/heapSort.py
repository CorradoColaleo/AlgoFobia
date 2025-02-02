import math

def MaxHeapify(A, i, dimA):
    left = (2 * i) + 1
    right = (2 * i) + 2
    largest = i

    if left < dimA and A[left] > A[largest]:
        largest = left

    if right < dimA and A[right] > A[largest]:
        largest = right

    if largest != i:  
        A[largest], A[i] = A[i], A[largest]
        MaxHeapify(A, largest, dimA)

def buildMaxHeap(A, dimA):
    middle = math.floor(len(A) / 2)

    while middle >= 0:
        MaxHeapify(A, middle, dimA)
        middle = middle - 1

def HeapSort(A):
    dimA = len(A)

    # Costruisci l'heap massimo
    buildMaxHeap(A, dimA)

    # Ordina l'array
    i = len(A)-i
    while i > 0:
        A[0], A[i] = A[i], A[0]  # Scambia il massimo (radice) con l'elemento alla fine
        dimA -= 1  # Riduci la dimensione dell'heap
        MaxHeapify(A, 0, dimA)  # Riapplica MaxHeapify alla radice
        i -= 1

if __name__ == "__main__":
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    HeapSort(A)
    print(A)
