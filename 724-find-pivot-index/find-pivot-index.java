class Solution {
    public int pivotIndex(int[] nums) {
        int tsum= 0;
        int left = 0;
        for(int i=0; i<nums.length; i++){
            tsum +=nums[i];
        }
        for(int j=0;j<nums.length;j++){
           int right = tsum-left-nums[j];
           if(left==right){
            return j;
           }
           left +=nums[j];
        }
        return -1;

    }
}