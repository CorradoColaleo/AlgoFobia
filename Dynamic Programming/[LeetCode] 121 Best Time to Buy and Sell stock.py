class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfitto = 0
        maxValore = prices[-1]
        for i in range(len(prices)-2,-1,-1):
            if maxValore-prices[i]>maxProfitto:
                maxProfitto = maxValore-prices[i]
            if prices[i]>maxValore:
                maxValore = prices[i]
        return maxProfitto

        