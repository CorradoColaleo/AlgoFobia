import java.util.ArrayList;
import java.util.List;

public class Solution {

    public List<List<Integer>> combine(int n, int k) {

        List<List<Integer>> result = new ArrayList<>();

        List<Integer> subvector = new ArrayList<>();

        Backtracking(result, subvector, k, n, 1);

        return result;

    }

    void Backtracking(List<List<Integer>> result, List<Integer> subvector, int k, int n, int start) {

        if (subvector.size()==k) {

            List<Integer> subvectorCopy = new ArrayList<>((subvector));

            result.add(subvectorCopy);

            return;

        }

        else {

            for (int i = start; i <= n; i++) {

                subvector.add(i);

                Backtracking (result, subvector, k, n , i + 1);

                subvector.remove(subvector.size() - 1);

            }

        }

    } 

}