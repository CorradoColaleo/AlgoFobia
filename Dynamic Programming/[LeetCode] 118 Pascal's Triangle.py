class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        if numRows >= 1:
            dp.append([1])
        if numRows >= 2:
            dp.append([1,1])
        if numRows>=3:
            for i in range(3,numRows+1):
                temp = []
                temp.append(1)
                for j in range(len(dp[-1])-1):
                    temp.append(dp[-1][j]+dp[-1][j+1])
                temp.append(1)
                dp.append(temp)
        return dp
        
        