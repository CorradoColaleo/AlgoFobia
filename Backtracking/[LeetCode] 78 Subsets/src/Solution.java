import java.util.concurrent.atomic.AtomicInteger;

public class Solution {

    boolean is_a_solution(boolean[] a, int k, int n) {
        return (k == n);
    }

    void construct_candidates(boolean[] a, int k, int n, boolean[] c, AtomicInteger nc) {
        c[0] = true;   // Candidato: includere l'elemento
        c[1] = false;  // Candidato: escludere l'elemento
        nc.set(2);     // Due candidati
    }

    void process_solution(boolean[] a, int k) {
        System.out.print("{ ");
        for (int i = 0; i < k; i++) {  // Cambiato <= con <
            if (a[i]) {
                System.out.print((i + 1) + " ");  // Stampa l'elemento i+1 (1-based index)
            }
        }
        System.out.println("}");  // Chiude la stampa del sottoinsieme
    }

    void backtracking(boolean[] a, int k, int n) {
        if (is_a_solution(a, k, n)) {
            process_solution(a, k);
        } else {
            boolean[] c = new boolean[2];
            AtomicInteger nc = new AtomicInteger();
            construct_candidates(a, k, n, c, nc);
            for (int i = 0; i < nc.get(); i++) {
                a[k] = c[i];  // Imposta il valore corrente (includi o escludi)
                backtracking(a, k + 1, n);  // Chiama ricorsivamente per il prossimo livello
            }
        }
    }

    public static void main(String[] args) {
        int n = 3;  // Numero di elementi dell'insieme {1, 2, 3}
        Solution solution = new Solution();
        boolean[] a = new boolean[n];  // Array per rappresentare il sottoinsieme
        solution.backtracking(a, 0, n);  // Inizia il backtracking
    }
}
