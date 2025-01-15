class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        lettere_alfabeto = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        result = []
        current = []
        self.backtracking(result,current,lettere_alfabeto,digits,0)
        return result

    def is_finished(self,current,ndigit):
        return (len(current)==ndigit)
    
    def construct_candidates(self,c,lettere_alfabeto,digits,step):
        for lettera in lettere_alfabeto[digits[step]]:
            c.append(lettera)
    
    def process_solution(self,current,result):
        result.append("".join(current))
    
    def backtracking(self,result,current,lettere_alfabeto,digits,step):
        if (self.is_finished(current,len(digits))):
            self.process_solution(current,result)
            return
        else:
            c = []
            self.construct_candidates(c,lettere_alfabeto,digits,step)
            for elem in c:
                current.append(elem)
                self.backtracking(result,current,lettere_alfabeto,digits,step+1)
                current.pop()    
        return
    

import unittest
from typing import List

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_letterCombinations_base_case(self):
        digits = ""
        expected = [""]
        self.assertEqual(self.solution.letterCombinations(digits), expected)

    def test_letterCombinations_single_digit(self):
        digits = "2"
        expected = ["a", "b", "c"]
        self.assertEqual(self.solution.letterCombinations(digits), expected)

    def test_letterCombinations_multiple_digits(self):
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(self.solution.letterCombinations(digits), expected)

    def test_letterCombinations_long_digits(self):
        digits = "234"
        expected = ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]
        self.assertEqual(self.solution.letterCombinations(digits), expected)

    def test_letterCombinations_digits_with_multiple_letters(self):
        digits = "7"
        expected = ["p", "q", "r", "s"]
        self.assertEqual(self.solution.letterCombinations(digits), expected)

if __name__ == '__main__':
    unittest.main()