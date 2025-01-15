import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;


/* QUESTA VERSIONE DELL'ESERCIZIO E' UNA MIA VARIANTE, NON CORRISPONDE EFFETTIVAMENTE
 * A QUANTO RICHIESTO DA LEETCODE (IN REALTA' E' ANCHE PIù DIFFICILE DI QUELLA PROPOSTA)
 */
public class Solution {
    public List<List<Integer>> findSubsequences(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        backtracking(result, current, nums);
        return result;
    }

    public void construct_candidates(List<Integer> current,int[] nums,int[]c, AtomicInteger nc){
        boolean[] used = new boolean[nums.length];

        for(int i=0;i<used.length;i++){
            used[i]=false;
        } 

        if (current.isEmpty()) {
            for (int i = 0; i < nums.length; i++) {
                c[i] = nums[i];
            }
            nc.set(nums.length);
            return;
        }

        for (int i=0;i<current.size();i++){
            for(int j=0;j<nums.length;j++){
                if (current.get(i).intValue() == nums[j] && used[j]==false){
                    used[j]=true;
                    break;
                }
            }
        }
        int lastNumber = current.get(current.size()-1).intValue();
        int index=0;
        for (int i=0;i<nums.length;i++){
            if (!used[i] && nums[i]>=lastNumber){
                c[index]=nums[i];
                index++;
                nc.set(nc.get()+1);
            }
        }  
    }

    public void backtracking(List<List<Integer>> result, List<Integer> current, int[] nums){
        if(current.size()>=2){
            List<Integer> copy = new ArrayList<>(current);
            if (!result.contains(copy)){
                result.add(copy);
            }
        }
        int[] c = new int[nums.length];
        AtomicInteger nc = new AtomicInteger();
        construct_candidates(current, nums, c, nc);
        for (int i=0;i<nc.get();i++){
            current.add(c[i]);
            backtracking(result, current, nums);
            current.remove(current.size()-1);
        }
    }

    public static void main(String[] args) {
        // Creiamo un'istanza della classe Solution
        Solution solution = new Solution();
        // Definiamo un array di numeri per il test
        int[] nums = {4, 6, 7, 7};
        // Chiamiamo il metodo findSubsequences
        List<List<Integer>> subsequences = solution.findSubsequences(nums);
        // Stampiamo tutte le sottosequenze crescenti trovate
        System.out.println("Sottosequenze crescenti di lunghezza >= 2:");
        for (List<Integer> subsequence : subsequences) {
            System.out.println(subsequence);
        }
    }
}
