class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        result = []
        print("Inizio ricerca dei percorsi...")
        self.backtracking(result, [0], graph)
        print("Ricerca completata.")
        return result

    def is_a_solution(self, current, graph):
        soluzione = (current[-1] == (len(graph) - 1))
        print(f"Verifico se {current} è una soluzione: {soluzione}")
        return soluzione

    def process_solution(self, result, current):
        print(f"Soluzione trovata: {current[:]}")
        result.append(current[:])

    def construct_candidates(self, c, current, graph):
        last_node = current[-1]
        candidati = graph[last_node]  # candidati è una lista
        print(f"Candidati per {last_node}: {candidati}")
        for candidato in candidati:
            c.append(candidato)

    def backtracking(self, result, current, graph):
        print(f"Stato attuale: {current}")
        if self.is_a_solution(current, graph):
            self.process_solution(result, current)
            return
        else:
            c = []
            self.construct_candidates(c, current, graph)
            for elemento in c:
                print(f"Aggiungo {elemento} al percorso")
                current.append(elemento)
                self.backtracking(result, current, graph)
                print(f"Rimuovo {elemento} dal percorso")
                current.pop()


# Funzione main per testare la classe Solution
if __name__ == "__main__":
    # Esempio di input
    graph = [[1, 2], [3], [3], []]
    
    soluzione = Solution()
    percorsi = soluzione.allPathsSourceTarget(graph)
    
    print("\nTutti i percorsi trovati:")
    for percorso in percorsi:
        print(percorso)
