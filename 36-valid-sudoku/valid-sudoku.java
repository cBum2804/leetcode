class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<String> got = new HashSet<>();
        
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                char curr_value= board[i][j];
                if(curr_value!='.'){
                    if(!got.add(curr_value + " found at row "+ i)||
                    !got.add(curr_value + " found at column " + j)||
                    !got.add(curr_value + " found at sub-box"+ i/3+ '-'+ j/3)) return false;
                }
            }
        }
        return true;
    }
}