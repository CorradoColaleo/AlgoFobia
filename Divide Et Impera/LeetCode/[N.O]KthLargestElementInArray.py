class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        max = None

        for i in range(k):

            max  = self.findMax(nums)

        print(f"The {k}th max is {max}")

        return max

    def findMax(self,nums: List[int]) -> int:

        max = nums[0]

        for k in nums:

            if max<k:

                max=k

        print(f"Now the max value is {max}")

        nums.remove(max)

        return max