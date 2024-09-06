class Solution {
    public int maxProfit(int[] prices) {
        int curr_price=prices[0];
        int profit=0;

        for(int i=1;i<prices.length;i++){

            if(curr_price>prices[i]){
                curr_price=prices[i];
            }
            
            profit = Math.max(prices[i]-curr_price,profit);
        }
        return profit;
    }
}