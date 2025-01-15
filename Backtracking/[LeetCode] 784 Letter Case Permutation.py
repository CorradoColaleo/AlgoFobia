import string

class Solution:
    def __init__(self):
        self.alfhabet = list(string.ascii_lowercase)
        self.alfhabet_upper = list(string.ascii_uppercase)

    def letterCasePermutation(self, s: str) -> list[str]:
        result = []
        current = ""
        self.backtracking(current,result,s,0)
        return result

    def is_a_solution(self,current,word):
        if (len(current)==len(word)):
            return True

    def process_solution(self,current,result):
        if current not in result:
            result.append(current)

    def backtracking(self,current,result,word,step):
        if (self.is_a_solution(current,word)):
            self.process_solution(current,result)
            print(current)
            return 
        else:
            temp = current
            if (word[step] in self.alfhabet):
                current = current + str.upper(word[step])
                self.backtracking(current,result,word,step+1)
                current = temp 
            elif (word[step] in self.alfhabet_upper):
                current = current + str.lower(word[step])
                self.backtracking(current,result,word,step+1)
                current = temp 
            current = current + word[step]
            self.backtracking(current,result,word,step+1)
            current = temp 

if __name__ == "__main__":
    # Creiamo un'istanza della classe Solution
    solution = Solution()
    
    # Esempio di input
    s = "C"
    
    # Chiamiamo il metodo letterCasePermutation e stampiamo il risultato
    permutations = solution.letterCasePermutation(s)
    print("Permutazioni di case:", permutations)