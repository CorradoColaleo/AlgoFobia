class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*n
        dp[-1]=arr[-1]
        for i in range(n-2,-1,-1):
            for j in range(1,k+1):
                if i+j>n:
                    break
                maxValue = max(arr[i:i+j])
                sommaMassima = maxValue*len(arr[i:i+j])
                if i+j>n-1:
                    dp[i]=max(dp[i],sommaMassima)
                else:
                    dp[i]=max(dp[i],sommaMassima+dp[i+j])
        return dp[0]
                

        