import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> result = new ArrayList<>();
        int totalNumbers = 1 << n; // Calcola 2^n
        for (int i = 0; i < totalNumbers; i++) {
            result.add(i ^ (i >> 1)); // Usa la formula Gray(i) = i ^ (i >> 1)
        }
        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> result = solution.grayCode(3);
        System.out.println("Gray Code sequence:");
        for (int num : result) {
            System.out.println(num);
        }
    }
}
