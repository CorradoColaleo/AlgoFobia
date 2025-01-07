class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        if root is None:
            return 0
        if root in dp:
            return dp[root]
        dp[root] = max(
            root.val +
            (self.rob(root.left.left) if root.left and root.left.left else 0) +
            (self.rob(root.left.right) if root.left and root.left.right else 0) +
            (self.rob(root.right.left) if root.right and root.right.left else 0) +
            (self.rob(root.right.right) if root.right and root.right.right else 0),
            self.rob(root.left) + self.rob(root.right)
        )
        return dp[root]