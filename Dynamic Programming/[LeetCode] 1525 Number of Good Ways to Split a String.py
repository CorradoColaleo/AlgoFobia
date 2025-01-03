class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        unique1 = []
        counter_unique1 = 0
        for i in range(n-1,-1,-1):
            if s[i] not in unique1:
                counter_unique1+=1
                dp[i]=counter_unique1
                unique1.append(s[i])
            else:
                dp[i]=dp[i+1]
        unique2=[]
        counter_unique2=0
        result=0
        for j in range(n-1):
            if s[j] not in unique2:
                counter_unique2+=1
                unique2.append(s[j])
            if counter_unique2 == dp[j+1]:
                result+=1
        return result

        