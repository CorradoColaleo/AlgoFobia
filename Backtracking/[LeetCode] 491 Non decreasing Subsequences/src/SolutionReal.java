import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

public class SolutionReal {
    
     public List<List<Integer>> findSubsequences(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        for (int i=0;i<used.length;i++){
            used[i]=false;
        }
        backtracking(result, current, nums,0,used);
        return result;
    }

    public void backtracking(List<List<Integer>> result, List<Integer> current, int[] nums, int step,boolean[] used){
        if(current.size()>=2){
            if (current.get(current.size()-1) < current.get(current.size()-2)){
                return;
            }
            List<Integer> copy = new ArrayList<>(current);
            if (!result.contains(copy)){
                result.add(copy);
            }
        }
        for (int i=step;i<nums.length;i++){
            if (i>0 && nums[i]<nums[i-1]){
                break;
            }
            if (!used[i]){
                used[i]=true;
                current.add(nums[i]);
                backtracking(result, current, nums,step+1,used);
                current.remove(current.size()-1);
                used[i]=false;
            }
            
        }
    }

    public static void main(String[] args) {
        // Creiamo un'istanza della classe Solution
        SolutionReal solution = new SolutionReal();
        // Definiamo un array di numeri per il test
        int[] nums = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
        // Chiamiamo il metodo findSubsequences
        List<List<Integer>> subsequences = solution.findSubsequences(nums);
        // Stampiamo tutte le sottosequenze crescenti trovate
        System.out.println("Stampo sottosequenze crescenti di lunghezza >= 2:");
        for (List<Integer> subsequence : subsequences) {
            System.out.println(subsequence);
        }
    }

}
