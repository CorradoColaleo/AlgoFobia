public class Solution {

    public char[][] solveSudoku(char[][] board) {

        char[][] solution = new char[9][9];

        Backtracking(board, solution, 0, 0, '0');

        return solution;

    }

    public boolean is_solution(char[][] board){
        for (int i=0;i<board.length;i++){
            for (int j=0;j<board.length;j++){
                if (board[i][j]=='.'){
                    return false;
                }
            }
        }
        return true;
    }

    public void printSudoku(char[][] board) {
        System.out.println();
        for (int i = 0; i < 9; i++) {
            // Stampa una linea divisoria ogni 3 righe (per separare i blocchi)
            if (i % 3 == 0 && i != 0) {
                System.out.println("------+-------+------");
            }
            for (int j = 0; j < 9; j++) {
                // Stampa una linea divisoria ogni 3 colonne (per separare i blocchi)
                if (j % 3 == 0 && j != 0) {
                    System.out.print(" | ");
                }
                // Stampa il valore della cella, sostituendo '0' o '.' con uno spazio vuoto
                System.out.print(board[i][j] == '0' || board[i][j] == '.' ? " " : board[i][j]);
                System.out.print(" ");
            }
            System.out.println();
        }
        System.out.println();

}

    public boolean is_valid(char[][]board, int i, int j, char candidate){
        // Controllo sui margini della matrice
        if ((i<0 || i>=board.length) || (j<0 || j>=board.length)){
            return false;
        }

        //Controllo sulla riga
        for (int index=0;index<board.length;index++){
            if (index != j && board[i][index]==candidate){
                return false;
            }
        }

        //Controllo sulla colonna
        for (int index=0;index<board.length;index++){
            if (index != i && board[index][j]==candidate){
                return false;
            }
        }

        //Controllo nel quadrato
        int rowCheck = 0;
        int columnCheck = 0;
        if (i >= 0 && i<= 2) {
            rowCheck = 0;
        } else if (i >=3 && i<=5) {
            rowCheck = 3;
        } else {
            rowCheck = 6;
        }
        if (j >= 0 && j <= 2) {
            columnCheck = 0;
        } else if (j >=3 && j<=5) {
            columnCheck = 3;
        } else {
            columnCheck = 6;
        }
        for (int row = rowCheck; row< rowCheck + 3;row++) {
            for (int column = columnCheck; column < columnCheck + 3;column++) {
                if (board[row][column] == candidate) {
                    if (row==i && column==j);
                    else{
                        return false;
                    }
                }
            }
        }
        return true;
    }

    public boolean Backtracking(char[][] board, char[][] solution,int i, int j, char candidate){
        if (is_valid(board,i,j,candidate)){
            if (is_solution(board)){
                for (int c = 0; c < board.length; c++) {
                    solution[c] = board[c].clone();
                }
                return true;
            }  
        }else{
            return false;
        }
        for (int row=0;row<board.length;row++){
            for (int column=0;column<board.length;column++){
                if (board[row][column] == '.'){
                    for (int num=1;num<=9;num++){
                            board[row][column]=(char)(num+'0');
                            if (Backtracking(board, solution, row, column, board[row][column])){
                                return true;
                            }
                            board[row][column]='.';
                    } return false;
                } 
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Esempio di board Sudoku incompleta
        char[][] board = {
            {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
            {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
            {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
            {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
            {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
            {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
            {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
            {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
            {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };

        // Creiamo una matrice vuota per la soluzione
        char[][] solutionBoard = new char[9][9];

        // Risolvi il Sudoku
        System.out.println("Sudoku iniziale:");
        solution.printSudoku(board);

        solutionBoard = solution.solveSudoku(board);

        System.out.println("\nSudoku risolto:");
        solution.printSudoku(solutionBoard);
    }
}
