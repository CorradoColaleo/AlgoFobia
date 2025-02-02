class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        dizionario = {}
        for elem in nums:
            try:
                dizionario[elem] +=1
            except:
                dizionario[elem] = 1
        chiave_massimo_valore = max(dizionario)
        lista = [0]*(range(0,chiave_massimo_valore))
        for chiave in dizionario.keys():
            lista[chiave]=dizionario[chiave]
        lista.sort(reverse=True)
        for i in range(k):
            result.append(lista[i])
        return result