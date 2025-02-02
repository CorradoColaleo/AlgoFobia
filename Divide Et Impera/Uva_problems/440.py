class Solution:

    def MakeOrderVector(self,n,m):

        if n<3 or n>=150:

            return "Error: n must be >=3 and <150"

        A = [1]

        visitedIndex = [0]

        currentIndex = 0

        while len(A) is not n:

            for i in range(m):

                currentIndex = (currentIndex+1)%n

                while currentIndex in visitedIndex:

                    currentIndex = (currentIndex+1)%n
            
            A.append(currentIndex+1)

            visitedIndex.append(currentIndex)
        
        return A[-1]

    def FindTheBestM(self,n,target):

        m = 1

        result = self.MakeOrderVector(n,m)

        while result is not target:

            m+=1

            result = self.MakeOrderVector(n,m)

        print("I have found the best m:",m)


s = Solution()

s.FindTheBestM(3,2)

s.FindTheBestM(4,2)

s.FindTheBestM(5,2)

s.FindTheBestM(6,2)

s.FindTheBestM(7,2)

s.FindTheBestM(8,2)

s.FindTheBestM(9,2)

s.FindTheBestM(10,2)

s.FindTheBestM(11,2)

s.FindTheBestM(12,2)








            

            










