class Solution:
    def stringCount(self, n: int) -> int:
        if n <= 3:
            return 0
        if n == 4:
            return 12
        dp = ["eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", "tlee"]
        alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in range(5, n + 1):
            counter = 0
            dp_temp = set()  
            for lettera in alfabeto:
                for parola in dp:
                    for j in range(len(parola) + 1): 
                        p = parola[:j] + lettera + parola[j:]
                        if p not in dp_temp:
                            dp_temp.add(p)
                            counter += 1
            dp = list(dp_temp)
        return counter
