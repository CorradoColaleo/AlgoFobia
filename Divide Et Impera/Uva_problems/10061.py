import math
class Solution:
    def solution(A,p,r,target):
        if (p==r):
            if target<A[p]:
                if p != 0:
                    return A[p-1],A[p]
                else:
                    return "X",A[p] 
            elif target>A[p]:
                return A[p],"X"
        q = math.floor((p+r)/2)
        if A[q] == target:
            if (0<q<len(A)-1):
                return A[q-1],A[q+1]
            elif q == 0 and q<len(A)-1:
                return "X",A[q+1]
            elif q == len(A)-1 and q>0:
                return A[q-1],"X"
            else:
                return None
        elif A[q]>target:
            return Solution.solution(A,p,q,target)
        else:
            return Solution.solution(A,q+1,r,target)
            
if __name__ == "__main__":
    test_cases = [
        {"A": [1, 4, 5, 7], "target": 3},
        {"A": [1, 4, 5, 7], "target": 5},
        {"A": [1, 4, 5, 7], "target": 8},
        {"A": [1, 4, 5, 7], "target": 0},
        {"A": [1, 2, 3, 4, 5], "target": 3},
        {"A": [1, 2, 3, 4, 5], "target": 6},
        {"A": [1], "target": 1},
        {"A": [1], "target": 2},
    ]

    for test_case in test_cases:
        A = test_case["A"]
        target = test_case["target"]
        try:
            risultato = Solution.solution(A, 0, len(A) - 1, target)
        except RecursionError:
            risultato = None
        print(f"Test case: A = {A}, target = {target}")
        print(f"Result: {risultato}")
        print()