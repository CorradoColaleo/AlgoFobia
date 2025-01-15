import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
        
        List<String> result = new ArrayList<>();

        Backtracking(result, 0, 0, "", n);

        return result;
    }

    public void Backtracking(List<String> result, int open, int closed, String current, int n) {

        if (open == n && closed == n) {

            result.add(current);

            return;

        }

        if (open < n) {

            Backtracking(result,open+1,closed,current + "(",n);

        }

        if (closed < open) {
            
            Backtracking(result, open, closed + 1, current + ")",n);
        }

    }
}
