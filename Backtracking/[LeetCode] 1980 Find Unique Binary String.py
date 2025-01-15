class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        result = self.backtracking("",nums)
        print(result)
        return result

    def is_finished(self,current,n):
        return (len(current)==n)
            
    def backtracking(self,current,nums):
        if self.is_finished(current,len(nums)):
            if current not in nums:
                return current
            else:
                return ""
        current += "0"
        result = self.backtracking(current,nums)
        if result =="":
            current = current[:-1]
            current +="1"
            result = self.backtracking(current,nums)
            current = current[:-1]
        return result

        
s = Solution()

s.findDifferentBinaryString(["00","10"])