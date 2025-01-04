class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count_one_zero(s: str) -> Tuple[int, int]:
            n1 = 0
            n0 = 0
            for elem in s:
                if elem == "0":
                    n0 += 1
                else:
                    n1 += 1
            return (n0, n1)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        for k in range(1, len(strs) + 1):
            n0, n1 = count_one_zero(strs[k - 1])
            for i in range(m + 1):
                for j in range(n + 1):
                    if i >= n0 and j >= n1:
                        dp[k][i][j] = max(dp[k - 1][i][j], dp[k - 1][i - n0][j - n1] + 1)
                    else:
                        dp[k][i][j] = dp[k - 1][i][j]
        return dp[len(strs)][m][n]
