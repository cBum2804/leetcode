class Solution {
    public int longestOnes(int[] nums, int k) {
        int max_zero=0; int left=0; int max_len=0;
        for(int right=0; right<nums.length; right++){
            if(nums[right]==0){
                max_zero++;
            }
            while(max_zero>k){
                if(nums[left]==0){
                    max_zero--;
                } left++;
            }
            max_len=Math.max(max_len, right-left+1);
        }
        return max_len;
    }
}