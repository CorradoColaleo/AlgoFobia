package LeetCode;

class Solution {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 4, 7, 11, 15},
            {2, 5, 8, 12, 19},
            {3, 6, 9, 16, 22},
            {10, 13, 14, 17, 24},
            {18, 21, 23, 26, 30}
        };
    
        int target = 5;
    
        boolean result = searchMatrix(matrix, target);
    
        System.out.println("Result: " + result);
    }

    public static boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        int colons = matrix[0].length;

        int i = 0;
        int j = colons-1;

        while(i < rows && j >= 0) {
            if(matrix[i][j] == target)
                return true;
            if(matrix[i][j] < target)
                i++;
            else if(matrix[i][j] > target)
                j--;
        }
        return false;
    }
}