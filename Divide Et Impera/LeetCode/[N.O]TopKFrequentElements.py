class Solution:

    def TopKFrequentElements(self, nums: list[int]):

        nums = sorted(nums)

        result = []

        i=0

        maxCount = 1

        currentCount = 1

        topElement = nums[0]
        
        currentElement = None

        if len(nums)==1:

            return [],topElement,maxCount

        for i in range (0,len(nums)-1):

            currentElement = nums[i]

            if nums[i]==nums[i+1]:

                currentCount+=1

            else:

                if currentCount > maxCount:

                    maxCount = currentCount

                    topElement = currentElement
            
                currentCount=1

        try:

            while True:

                nums.remove(topElement)

        except ValueError:

            pass

        return nums,topElement,maxCount

    def CompleteTopKFrequentElements(self,nums: list[int],k):

        listOfResult = []

        for i in range(k):

            nums,topElement,maxCount = self.TopKFrequentElements(nums)

            listOfResult.append(topElement)

        return listOfResult

l = [1,2,3,4]

s = Solution()

r = s.CompleteTopKFrequentElements(l,3)

print(r)
