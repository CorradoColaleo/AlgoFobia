# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def averageOfSubtree(self, root: TreeNode) -> int:

        result = 0

        if (root.left) is None and (root.right) is None:

            return 1

        else:

            sumSubtree, num = self.sum(root)

            avarage = int(sumSubtree/num)

            if root.val == avarage:

                result +=1

            if root.left is not None:

                result += self.averageOfSubtree(root.left)

            if root.right is not None:

                result += self.averageOfSubtree(root.right)

        return result
            

        
    def sum(self, root):

        if (root.left) is None and (root.right) is None:

            return root.val,1

        elif (root.left) is not None and (root.right) is None:

            sumLeft,counter = self.sum(root.left)

            return sumLeft + root.val, counter+1

        elif (root.left) is None and (root.right) is not None:

            sumRight,counter = self.sum(root.right)

            return sumRight + root.val,counter+1

        else:

            sumLeft,counter1 = self.sum(root.left)

            sumRight,counter2 = self.sum(root.right)

            return sumRight + sumLeft + root.val, counter1+counter2+1





        