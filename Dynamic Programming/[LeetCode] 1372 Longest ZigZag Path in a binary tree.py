class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        dp = {}  # Dizionario per la memoizzazione
        
        def solution(node, direction, length):
            if not node:
                return length - 1  # Termina e ritorna la lunghezza del percorso
            if (node, direction) in dp:
                return dp[(node, direction)]
            
            # Calcola il percorso zig-zag
            if direction == "right":
                left_zigzag = solution(node.left, "left", length + 1)
                right_reset = solution(node.right, "right", 1)
                dp[(node, direction)] = max(left_zigzag, right_reset)
            else:  # direction == "left"
                right_zigzag = solution(node.right, "right", length + 1)
                left_reset = solution(node.left, "left", 1)
                dp[(node, direction)] = max(right_zigzag, left_reset)
            
            return dp[(node, direction)]
        
        # Calcola il risultato massimo esplorando entrambi i lati
        return max(solution(root, "left", 0), solution(root, "right", 0))
