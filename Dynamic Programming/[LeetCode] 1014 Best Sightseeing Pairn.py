class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        if len == 2:
            return values[0]+values[1]-1
        n = len(values)
        result = values[-2]+values[-1]-1
        diffMassima = max((values[-1]-(n-1)),(values[-2]-(n-2)))
        for i in range(n-3,-1,-1):
            result = max(result,(values[i]+i+diffMassima))
            if (values[i]-i)>diffMassima:
                diffMassima = values[i]-i
        return result