class Solution {
    public int maxOperations(int[] nums, int k) {
        int left = 0;
        int right = nums.length-1; 
        int count = 0;

        Arrays.sort(nums);

        while(left<right){
            int sum = nums[left]+nums[right];

            if(sum<k){
                left++;
            }
            else if(sum>k){
                right--;
            }
            else{
                left++;
                right--;
                count++;
            }
    }
    return count;
}
}