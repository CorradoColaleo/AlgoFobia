class Solution:

    def countSmaller(self, nums: list[int]) -> list[int]:

        result = []
        
        for i in range(len(nums)):

            counter = 0

            for j in range(i,len(nums)):

                if nums[i]>nums[j]:

                    print(f"{nums[i]}<{nums[j]}")

                    counter+=1

            result.append(counter)

        return result


s = Solution()

print(s.countSmaller([-1,-1]))



