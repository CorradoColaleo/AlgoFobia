import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

public class Solution {

    public List<String> validStrings(int n) {
        List<String> result = new ArrayList<>();
        String current = new String();
        backtracking(result, current, n, 0);
        return result;
    }

    public boolean is_a_solution(String current, int n) {
        for (int i=0;i<current.length();i++){
            if (current.charAt(i) == '0' && (i!=(n-1))){
                if (current.charAt(i+1)=='0'){
                    return false;
                }
            }
        }
        return true;
    }

    public boolean is_finished(String current, int n) {
        return (current.length() == n);
    }

    public void process_solution(List<String> result, String current){
        String copy = new String(current);
        result.add(copy);
    }

    public void construct_candidates(String current,int k,int[]c, AtomicInteger nc){
        c[0]=0;
        c[1]=1;
        nc.set(2);
    }
    public void backtracking(List<String> result,String current, int n, int k) {
        if (is_finished(current, n)){
            if (is_a_solution(current, n)){
                process_solution(result, current);
            }
            return;
        } else {
            int[] c = new int[2];
            AtomicInteger nc = new AtomicInteger();
            construct_candidates(current, k , c, nc);
            for (int i=0;i<nc.get();i++){
                current = current.substring(0, k) + String.valueOf(c[i]) + current.substring(k,current.length());
                backtracking(result, current, n, k+1);
                current = current.substring(0, k) +  current.substring(k+1,current.length());
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 3; // Modifica il valore di n per generare stringhe di diversa lunghezza
        List<String> result = solution.validStrings(n);
        System.out.println("Stringhe valide di lunghezza " + n + ":");
        for (String s : result) {
            System.out.println(s);
        }
    }
}