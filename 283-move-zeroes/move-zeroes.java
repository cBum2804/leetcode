class Solution {
    public void moveZeroes(int[] nums) {
      //int count1=nums[1];
      int left=0;
      
      for(int right =0;right<nums.length;right++){
        if(nums[right]!=0){
            int temp= nums[right];
            nums[right]=nums[left];
            nums[left]=temp;
            left++;
        }
        }
    }
}