class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        int[][] board = new int[rows][columns];
        
        int number = 1;
        
        for (int i = 0; i < rows; i++){
            for (int j = 0; j < columns; j++){
                 board[i][j] = number++;
            }
        }
        
        int[] answer = new int[queries.length];
        
        for (int q = 0; q < queries.length; q++){
            int x1 = queries[q][0] -1;
            int y1 = queries[q][1] -1;
            int x2 = queries[q][2] -1;
            int y2 = queries[q][3] -1;
            
            int temp = board[x1][y1];
            int min = temp;
            
            // 왼쪽변 : 아래숫자를 위로
            for (int i = x1; i < x2; i++){
                board[i][y1] = board[i+1][y1];
                min = Math.min(min, board[i][y1]);
            }
            
            // 아래쪽변 : 오른쪽 -> 왼쪽
            for (int j = y1; j < y2; j++){
                board[x2][j] = board[x2][j+1];
                min = Math.min(min, board[x2][j]);
            }
            
            // 오른쪽변 : 위 숫자를 아래로
            for (int i = x2; i > x1; i--){
                board[i][y2] = board[i-1][y2];
                min = Math.min(min, board[i][y2]);
            }
            
            // 위쪽변 : 왼쪽 -> 오른쪽
            for (int j = y2; j > y1; j--){
                board[x1][j] = board[x1][j-1];
                min = Math.min(min, board[x1][j]);
            }
            
            board[x1][y1+1] = temp;
            
            answer[q]= min;
        }
        return answer;
    }
}