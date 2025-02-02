class Solution:
    def hammingWeight(self, n: int) -> int:
        b = str(bin(n))
        binary_representation = b[2:len(b)]
        print(binary_representation)
        counter = 0
        for bit in binary_representation:
            if bit == "1":
                counter+=1
        return counter