class Solution:
    def minDays(self, n: int) -> int:
        memo = {}
        for i in range(1, n + 1):
            if i == 1:
                memo[i] = 1
            elif i == 2:
                memo[i] = 2
            elif i == 3:
                memo[i] = 2
            else:
                if (i % 2) == 0 and (i % 3) == 0:
                    memo[i] = min(
                        1 + memo[i - 1],
                        1 + memo[i - (i // 2)],
                        1 + memo[i - (2 * (i // 3))]
                    )
                elif (i % 2) == 0 and (i % 3) != 0:
                    memo[i] = min(
                        1 + memo[i - 1],
                        1 + memo[i - (i // 2)],
                    )
                elif (i % 2) != 0 and (i % 3) == 0:
                    memo[i] = min(
                        1 + memo[i - 1],
                        1 + memo[i - (2 * (i // 3))]
                    )
                else:
                    memo[i] = 1 + memo[i - 1]
        return memo[n]


#Da notare che su leetcode questo non viene accettato per TLE. Ho provato
#anche a portarlo in java ma da Memory Limit! La logica comunque resta corretta
# con il DP