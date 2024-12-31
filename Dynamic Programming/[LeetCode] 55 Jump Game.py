class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Caso base: se l'array ha un solo elemento, possiamo sempre raggiungere la fine
        if len(nums) == 1:
            return True

        # Inizializziamo l'array dp per tenere traccia delle posizioni raggiungibili
        dp = [False] * len(nums)
        dp[-1] = nums[-1] != 0  # L'ultima posizione è raggiungibile solo se il valore non è 0

        # Iteriamo all'indietro per determinare la raggiungibilità di ogni posizione
        for i in range(len(nums) - 2, -1, -1):
            # Se nums[i] è 0, questa posizione non è raggiungibile
            if nums[i] == 0:
                dp[i] = False
            else:
                # Controlliamo se da questa posizione possiamo raggiungere una posizione valida
                for j in range(1, nums[i] + 1):
                    if i + j >= len(nums) - 1 or dp[i + j]:
                        dp[i] = True
                        break

        # La prima posizione deve essere raggiungibile
        return dp[0]
