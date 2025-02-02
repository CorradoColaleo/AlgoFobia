# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"{self.val},{self.next}"

class Solution:

    def sortList(self, head: ListNode):
        
        listOfNode = []

        currentNode = head 

        while currentNode.next is not None:

            listOfNode.append(currentNode)

            currentNode = currentNode.next

        listOfNode.append(currentNode)

        self.mergeSort(listOfNode,0,len(listOfNode)-1)

        print(listOfNode[0])

    def mergeSort(self,A, p, r):

        if p < r:

            q = (p + r) // 2  # Divisione intera in Python

            self.mergeSort(A, p, q)

            self.mergeSort(A, q + 1, r)

            self.merge(A, p, q, r)
            
    def merge(self, A, p, q, r):
            
        n1 = q - p + 1

        n2 = r - q
        
        L = A[p:q+1]  # L contiene A[p] fino ad A[q]

        R = A[q+1:r+1]  # R contiene A[q+1] fino ad A[r]

        firstL = ListNode(float('inf'))

        firstR = ListNode(float('inf'))
        
        L.append(firstL)

        R.append(firstR)
        
        i = 0  # Indice iniziale di L

        j = 0  # Indice iniziale di R
            
        for k in range(p, r+1):

            if L[i].val <= R[j].val:

                A[k] = L[i]

                i += 1

            else:

                A[k] = R[j]

                j += 1

        for index in range(len(A)-1):

            A[index].next=A[index+1]

        A[len(A)-1].next=None

        
            


s = Solution()

s = Solution()

# Creazione della lista iniziale
head = ListNode(4)

head.next = ListNode(2)

head.next.next = ListNode(1)

head.next.next.next = ListNode(3)

# Ordinamento della lista e stampa del risultato
sorted_list = s.sortList(head)





