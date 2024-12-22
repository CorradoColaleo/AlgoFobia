class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float("inf")] * len(days)  
        return self.solution(dp, 0, costs, days)
    
    def solution(self, dp: List[int], index: int, costs: List[int], days: List[int]) -> int:
        if index >= len(days):
            return 0        
        if dp[index] != float("inf"):
            return dp[index]
        dp[index] = min(
            costs[0] + self.solution(dp, self.next_index(index, days[index] + 1, days), costs, days),
            costs[1] + self.solution(dp, self.next_index(index, days[index] + 7, days), costs, days),
            costs[2] + self.solution(dp, self.next_index(index, days[index] + 30, days), costs, days)
        )
        return dp[index]  
    
    def next_index(self, current: int, coverage_end: int, days: List[int]) -> int:
        while current < len(days) and days[current] < coverage_end:
            current += 1
        return current
