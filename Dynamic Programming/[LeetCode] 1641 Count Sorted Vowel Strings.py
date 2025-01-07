class Solution:
    def countVowelStrings(self, n: int) -> int:
        startList = ["a", "e", "i", "o", "u"]
        if n == 1:
            return len(startList)

        vowels = {
            "a": 1,
            "e": 2,
            "i": 3,
            "o": 4,
            "u": 5
        }

        def solution(startList, vowels):
            endList = []
            for vowel in vowels.keys():
                for elem in startList:
                    if vowels[vowel] <= vowels[elem[0]]:
                        endList.append(vowel + elem)
            return endList

        for i in range(2, n + 1):
            startList = solution(startList, vowels)

        return len(startList)

