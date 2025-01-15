class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        result = []
        self.backtracking(0, 0, s, result, [])
        return len(result)
        
    def backtracking(self, index, step, s, result, current):

        flag = True
        
        # Condizione di fine
        if step == len(s):
            if len("".join(current)) == len(s):
                if len(current) > len(result):
                    result[:] = current[:]  # Copio il contenuto di current in result
            return

        if s[index:step+1] in current:

            flag = False  
        else:
         
            current.append(s[index:step+1])
        
        if flag:

            self.backtracking(step+1, step+1, s, result, current)

            current.pop()

        self.backtracking(index, step+1, s, result, current)
