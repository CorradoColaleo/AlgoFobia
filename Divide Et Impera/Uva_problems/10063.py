class Solution:
    def solution(self, stringa):
        result = []
        print(f"Inizio generazione permutazioni per: {stringa}")  # Stampa di inizio
        self.backtracking(result, [], stringa)
        print(f"Permutazioni trovate {len(result)}:")
        print(result)

    def is_finished(self, result, current, stringa):
        if (len(current) == len(stringa)):
            if (current not in result):
                result.append(current[:])
            return True
        return False

    def construct_candidates(self, c, stringa, current):
        used = [False] * len(stringa)
        j = 0
        for i in range(len(stringa)):
            if stringa[i] in current:
                used[i]=True
        for i in range(len(used)):
            if used[i] == False:
                c.append(stringa[i])

    def backtracking(self, result, current, stringa):
        if (self.is_finished(result, current, stringa)):
            return
        c = []
        self.construct_candidates(c, stringa, current)
        if len(c) == 0:
            return
        candidato = c[0]
        if (len(current) == 0):
            current.append(candidato)
            self.backtracking(result, current, stringa)
        else:
            current = [candidato] + current
            self.backtracking(result, current, stringa)
            for i in range(1, len(current)):
                temp = current[i]
                current[i] = current[i - 1]
                current[i - 1] = temp
                self.backtracking(result, current, stringa)

if __name__ == "__main__":
    s = Solution()
    s.solution("abc")
    s.solution("bca")
    s.solution("dcba")
