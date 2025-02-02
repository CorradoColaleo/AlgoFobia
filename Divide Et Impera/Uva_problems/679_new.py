class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.flag = False

class Solution:
    def countNodes(self, D, k):
        root = self.construct_tree(D)
        for i in range(k):
            result = self.recursion(root)
        print(result)
        return result

    def recursion(self,node):
        if node.left is None and node.right is None:
            return node.val 
        if node.flag == True:
            node.flag = False
            return self.recursion(node.right)
        else:
            node.flag = True
            return self.recursion(node.left)

    def construct_tree(self,D):
        lista_nodi = []
        if D == 0:
            return None
        else:
            for i in range(1,2**D):
                lista_nodi.append(Node(i))
            for i in range(2**D):
                if 2*i+1 < 2**D - 1:
                    lista_nodi[i].left = lista_nodi[2*i+1]
                if 2*i+2 < 2**D - 1:
                    lista_nodi[i].right = lista_nodi[2*i+2]
            return lista_nodi[0]
    
    def print_tree(self,node):
        if node is None:
            return
        else:
            print(node.val)
            self.print_tree(node.left)
            self.print_tree(node.right)

if __name__=="__main__":
    s = Solution()
    s.countNodes(4,2)
    s.countNodes(3,4)
    s.countNodes(10,1)
    s.countNodes(2,2)
    s.countNodes(8,128)