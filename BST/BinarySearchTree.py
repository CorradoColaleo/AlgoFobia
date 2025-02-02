class node:

    def __init__(self, val, p = None, left = None, right = None):

        self.val = val

        self.p = p

        self.left = left 

        self.right = right

    def __str__(self):

        padre = self.p.val if self.p else "Nessuno"

        left = self.left.val if self.left else "Nessuno"

        right = self.right.val if self.right else "Nessuno"

        return f"Valore = {self.val}, Padre = {padre}, Figlio_Sinistro = {left}, Figlio_Destro = {right}"


class BinarySearchTree:

    @staticmethod
    def Inorder_Tree_Walk(root):

        if root is not None:

            BinarySearchTree.Inorder_Tree_Walk(root.left)

            print(root.val)

            BinarySearchTree.Inorder_Tree_Walk(root.right)
        
        #Complessità: O(n)

    @staticmethod
    def Tree_Search(root,val):

        if (root is None) or (root.val == val):

            return root

        elif root.val > val:

            return BinarySearchTree.Tree_Search(root.left,val)

        else:

            return BinarySearchTree.Tree_Search(root.right,val)

        #Complessità: O(h) con h altezza dell'albero 

    @staticmethod
    def Iterative_tree_search(root,val):

        while (root is not None) and root.val != val:

            if root.val > val:

                root = root.left 
            
            else:

                root = root.right

        return root

        #Complessità: O(h) con h altezza dell'albero 

    @staticmethod
    def Tree_minimum(root):

        min = root

        while root is not None:

            min = root

            root = root.left

        print(f"[TREE_MINIMUM] Min = {min}")

        return min

        #Complessità: O(h) con h altezza dell'albero 


    @staticmethod
    def Tree_maximum(root):

        max = root

        while root is not None:

            max = root

            root = root.right

        print(f"[TREE_MAXIMUM] Max = {max}")

        return max

    #Complessità: O(h) con h altezza dell'albero 

    @staticmethod
    def Successor(node):

        #successore = elemento che lo segue (se sono numeri, il primo elemento più grande)

        print(node)

        if node.right is not None:

            return BinarySearchTree.Tree_minimum(node.right)

        else:

            y = node.p

            while (y is not None) and (node == y.right):

                x = y 

                y = y.p 

                print(x)

                print(y)

            return y 

    # Complessità : O(h) con h altezza dell'albero

    @staticmethod
    def Tree_insert(root,nodeToInsert):

        y = None

        x = root 

        while x is not None:

            y = x 

            if nodeToInsert.val > x.val: 

                x = x.right 

            else: 

                x = x.left 

        nodeToInsert.p = y 

        if y==None:

            root = z 

        else:

            if nodeToInsert.val < y.val:

                y.left = nodeToInsert

            else:

                y.right = nodeToInsert
        
    #Complessità: O(h) con h altezza dell'albero 

    @staticmethod
    def Tree_delete(root,nodeToDelete):

        y = None 

        x = None

        if (nodeToDelete.left is None) or (nodeToDelete.right is None):

            y = nodeToDelete
        
        else:

            y = BinarySearchTree.Successor(nodeToDelete)

        if y.left is not None:

            x = y.left 

        else:

            x = y.right

        if y.p is None:

            root = x 

        elif y == y.p.left:

            y.p.left = x

        else:

            y.p.right = x 

        if y != nodeToDelete:

            nodeToDelete.val = y.val 

        return y 

    #Complessità: O(h) con h altezza dell'albero 




def costruisciAlbero():
    
    # Creiamo i nodi
    root = node(5)
    node1 = node(3)
    node2 = node(7)
    node3 = node(2)
    node4 = node(5)
    node5 = node(8)

    # Costruzione dell'albero binario di ricerca
    root.left = node1
    root.right = node2
    node1.p = root
    node2.p = root
    node1.left = node3
    node1.right = node4
    node3.p = node1 
    node4.p = node1
    node2.right = node5
    node5.p = node2
    
    return root 

def mainPrint():
    
    root = costruisciAlbero()

    print("Inorder traversal:")

    BinarySearchTree.Inorder_Tree_Walk(root)

def mainTreeSearch(k):

    root = costruisciAlbero()

    node = BinarySearchTree.Tree_Search(root,k)

    print(f"Tree search, val={k}: {node}")

    node = BinarySearchTree.Iterative_tree_search(root,k)

    print(f"Iterative tree search, val={k}: {node}")

def mainSuccessor():

    # Creiamo i nodi
    root = node(15)
    node1 = node(6)
    node2 = node(18)
    node3 = node(3)
    node4 = node(7)
    node5 = node(17)
    node6 = node(20)
    node7 = node(2)
    node8 = node(4)
    node9 = node(13)
    node10 = node(9)

    # Costruzione dell'albero binario di ricerca
    root.left = node1
    root.right = node2
    node1.p = root
    node2.p = root
    node1.left = node3
    node1.right = node4
    node3.p = node1 
    node4.p = node1
    node2.left = node5
    node2.right = node6
    node5.p = node2
    node6.p = node2 
    node3.left = node7
    node3.right = node8
    node7.p = node3
    node8.p = node3 
    node4.right=node9 
    node9.p = node4 
    node9.left = node10 
    node10.p = node9

    successor = BinarySearchTree.Successor(node1)

    print(f"{node1.val}'s successor: {successor}")

def mainInsert(z):

    nodeToInsert = node(z)

    # Creiamo i nodi
    root = node(15)
    node1 = node(6)
    node2 = node(18)
    node3 = node(3)
    node4 = node(7)
    node5 = node(17)
    node6 = node(20)
    node7 = node(2)
    node8 = node(4)
    node9 = node(13)
    node10 = node(9)

    # Costruzione dell'albero binario di ricerca
    root.left = node1
    root.right = node2
    node1.p = root
    node2.p = root
    node1.left = node3
    node1.right = node4
    node3.p = node1 
    node4.p = node1
    node2.left = node5
    node2.right = node6
    node5.p = node2
    node6.p = node2 
    node3.left = node7
    node3.right = node8
    node7.p = node3
    node8.p = node3 
    node4.right=node9 
    node9.p = node4 
    node9.left = node10 
    node10.p = node9

    BinarySearchTree.Tree_insert(root,nodeToInsert)

    print(f"Insert {z}: {nodeToInsert}")

def mainDelete():

    # Creiamo i nodi
    root = node(15)
    node1 = node(6)
    node2 = node(18)
    node3 = node(3)
    node4 = node(7)
    node5 = node(17)
    node6 = node(20)
    node7 = node(2)
    node8 = node(4)
    node9 = node(13)
    node10 = node(9)

    # Costruzione dell'albero binario di ricerca
    root.left = node1
    root.right = node2
    node1.p = root
    node2.p = root
    node1.left = node3
    node1.right = node4
    node3.p = node1 
    node4.p = node1
    node2.left = node5
    node2.right = node6
    node5.p = node2
    node6.p = node2 
    node3.left = node7
    node3.right = node8
    node7.p = node3
    node8.p = node3 
    node4.right=node9 
    node9.p = node4 
    node9.left = node10 
    node10.p = node9

    BinarySearchTree.Tree_delete(root,node1)

    BinarySearchTree.Inorder_Tree_Walk(root)


if __name__ == "__main__":
    #mainPrint()
    #mainTreeSearch(3)
    #mainSuccessor()   
    #mainInsert(19)
    mainDelete()