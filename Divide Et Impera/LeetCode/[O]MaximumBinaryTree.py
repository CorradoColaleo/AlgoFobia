# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"{self.val}"

class Solution:

    def constructMaximumBinaryTree(self, nums: list[int]):

        if len(nums)==0:

            return None
            
        max,index = self.find_max(nums)

        radix = TreeNode()

        radix.val=max

        radix.left = self.constructMaximumBinaryTree(nums[0:index])

        radix.right = self.constructMaximumBinaryTree(nums[index+1:len(nums)])

        print(f"Radix = {radix}, left = {radix.left}, right = {radix.right}")

        return radix

    def find_max(self,nums):

        max = float("-inf")

        index = 0

        for i in range(len(nums)):

            if nums[i]>max:

                max = nums[i]

                index = i

        return max,index


s = Solution()
print(s.constructMaximumBinaryTree([3,2,1,6,0,5]))