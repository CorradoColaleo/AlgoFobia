class Solution:

    def solution(self,stringa,k):
        result = []
        result.append(stringa)
        self.backtracking(k,0,0,stringa,result)
        result.sort()
        print(len(result))
        print(result)

    def is_finished(self,k,n_cambiati,indice_colonna,lunghezza_stringa):
        return ((k==n_cambiati) or (indice_colonna==lunghezza_stringa))
    
    def process_solution(self,result,stringa):
        if stringa not in result:
            result.append(stringa)
    
    def construct_candidates(self,c,lettera_corrente):
        lista = ["A","G","C","T"]
        for elemento in lista:
            if elemento != lettera_corrente:
                print(f"[DEBUG] Ho aggiunto {elemento} nella stringa")
                c.append(elemento)
    
    def backtracking(self,k,n_cambiati,indice_colonna,stringa,result):
        if (self.is_finished(k,n_cambiati,indice_colonna,len(stringa))):
            if (k==n_cambiati):
                self.process_solution(result,stringa)
            return
        else:
            c = []
            self.construct_candidates(c,stringa[indice_colonna])
            self.backtracking(k,n_cambiati,indice_colonna+1,stringa,result)
            for candidato in c:
                temp = stringa
                lista_stringa = list(stringa)
                lista_stringa[indice_colonna]=candidato
                stringa = "".join(lista_stringa)
                self.backtracking(k,n_cambiati+1,indice_colonna+1,stringa,result)
                stringa = temp
            

if __name__=="__main__":

    s = Solution()

    s.solution("AAA",1)

    s.solution("AAA",2)