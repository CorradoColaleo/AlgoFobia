import math

class Solution:

    def majorityElement(self, nums: list[int]) -> int:
        
        dizionario = {}

        for elem in nums:

            try:

                dizionario[elem]=0
            
            except:

                pass

        for num in nums:

            dizionario[num]+=1

        finalKey = None

        max = float("-inf")

        for key in dizionario.keys():

            if dizionario[key]>max:

                max = dizionario[key]

                finalKey=key
        
        print(finalKey)

        return finalKey            

if __name__=="__main__":

    s = Solution()

    print(s.majorityElement([2,2,1,1,1,2,2]))