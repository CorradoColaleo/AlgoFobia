class Solution:

    def solution(self, n, input_m, last_value, dx_value):
        inseriti = []
        print(f"Starting solution with n={n}, pieces={input_m}, start={last_value}, end={dx_value}")
        if self.backtracking(inseriti, input_m, n, last_value, dx_value):
            print("YES")
        else:
            print("NO")
        print("Solution pieces:", inseriti)

    def is_a_solution(self, n, inseriti):
        return n == len(inseriti)

    def is_finished(self, n, last_value, input_m, dx_value, inseriti):
        c = []
        nc = 0  # Use a simple counter for number of candidates
        nc, c = self.construct_candidates(n, nc, c, last_value, input_m, dx_value, inseriti)
        return n == len(inseriti) or not c  # Return True if we've filled all spaces or no candidates left

    def construct_candidates(self, n, nc, c, last_value, input_m, dx_value, inseriti):
        if len(inseriti) != n - 1:  # If we haven't filled all spaces yet
            print(f"Constructing candidates for last_value={last_value}, inseriti={inseriti}")
            for i in range(len(input_m)):
                if last_value == input_m[i][0]:  # We can place the piece as it is
                    c.append(input_m[i])
                    nc += 1
                    print(f"Adding candidate {input_m[i]} (no rotation)")
                elif last_value == input_m[i][1]:  # We can rotate the piece
                    temp = (input_m[i][1], input_m[i][0])
                    c.append(temp)
                    nc += 1
                    print(f"Adding candidate {temp} (rotated)")
            return nc, c
        else:
            print(f"Looking for the last piece that matches {last_value} and {dx_value}")
            for i in range(len(input_m)):
                if input_m[i][0] == last_value and input_m[i][1] == dx_value:
                    return 1, [input_m[i]]
                elif input_m[i][1] == last_value and input_m[i][0] == dx_value:
                    return 1, [(input_m[i][1],input_m[i][0])]
            return 0, []

    def backtracking(self, inseriti, input_m, n, last_value, dx_value):
        print(f"Backtracking: inseriti={inseriti}, input_m={input_m}, last_value={last_value}, dx_value={dx_value}")
        if self.is_finished(n, last_value, input_m, dx_value, inseriti):
            if self.is_a_solution(n, inseriti):
                print(f"Found solution: {inseriti}")
                return True
            else:
                print("Finished but not a valid solution")
                return False
        else:
            nc = 0
            c = []
            nc, c = self.construct_candidates(n, nc, c, last_value, input_m, dx_value, inseriti)
            if not c:
                print(f"No valid candidates for last_value={last_value}")
                return False
            for candidate in c:
                print(f"Trying candidate {candidate}")
                inseriti.append(candidate)
                # Remove the candidate from the list
                if candidate in input_m:
                    input_m.remove(candidate)
                else:
                    input_m.remove((candidate[1], candidate[0]))  # If it was rotated
                # Make the recursive call
                if self.backtracking(inseriti, input_m, n, candidate[1], dx_value):
                    return True
                else:
                    # If not a valid solution, backtrack
                    inseriti.pop()
                    input_m.append(candidate)
                    print(f"Backtracking, removing candidate {candidate}")
            return False


if __name__ == "__main__":

    s = Solution()

    # First test case
    print("Test case 1:")
    s.solution(3, [(2, 1), (5, 6), (3, 2), (2, 2)], 1, 3)

    # Second test case
    print("\nTest case 2:")
    s.solution(2, [(1, 4), (4, 4), (3, 2), (5, 6)], 1, 3)
