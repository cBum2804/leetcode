class Solution {
    public double calculateTax(int[][] brackets, int income) {
        double output=0;
        double prev= 0;
        if(income==0){
            return 0;
        }
        if(income<=brackets[0][0]){
            return (double) brackets[0][1]*income/100;
        }

        for(int i = 0; i<brackets.length; i++){
            if(income> brackets[i][0]){
                output += (brackets[i][0]-prev)*brackets[i][1]/100;
                prev = brackets[i][0];
            }
            else{
                output +=(income-prev)*brackets[i][1]/100;
                break;
            }
        }
        return output;
    }
}