class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        if n==1:
            return books[0][1]
        dp = [float("inf")]*n
        dp[-1] = books[-1][1]
        for i in range(n-2,-1,-1):
            dp[i]=books[i][1]+dp[i+1]
            temp = books[i][0]
            massimo = books[i][1]
            for j in range(i+1,n):
                temp += books[j][0]
                if temp>shelfWidth:
                    break
                massimo = max(massimo,books[j][1])
                if j+1<n:
                    dp[i]=min(dp[i],massimo+dp[j+1])
                else:
                    dp[i]=min(dp[i],massimo)
        return dp[0]
