import java.util.concurrent.atomic.AtomicInteger;

public class Solution {

    boolean is_a_solution(int k, int n) {

        return (k==n);

    }

    void construct_candidates(int a[], int k, int[] c, AtomicInteger nc, int n) {

        int index = 0;

        boolean [] used = new boolean[n];

        for (int i=0;i<used.length;i++) {

            used[i] = false;

        }

        for (int i=0;i<k;i++) {
        
            used[a[i] - 1] = true; 

        }

        for (int i=0;i<used.length;i++) {
            
            if (used[i] == false) {

                c[index] = (i+1);
                
                index+=1;

                nc.set((nc.get())+1);
            }

        }

    }

    void process_solution(int[] a){

        System.out.print("{");

        for (int i=0;i<a.length;i++) {

            System.out.print(a[i]);

            System.out.print(" ");

        }

        System.out.println("}");


    }

    void backtracking(int[] a, int k, int n){

        if (is_a_solution(k, n)){

            process_solution(a);

        } else {

            int[] c = new int[n];

            AtomicInteger nc = new AtomicInteger();

            construct_candidates(a, k, c, nc, n);

            for (int i=0;i<nc.get();i++){

                a[k] = c[i];

                backtracking(a, k+1, n);

            }

        }

    }

    public static void main(String[] args) {
        int n = 3;  // Numero di elementi dell'insieme {1, 2, 3}
        Solution solution = new Solution();
        int[] a = new int[n];  // Array per rappresentare i sottoinsiemi
        solution.backtracking(a, 0, n);  // Inizia il backtracking
    }
    
}
