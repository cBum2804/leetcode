class Solution {
    public int jump(int[] nums) {
        int left=0;;
        int right=0;
        int jump=0;
        while(right<nums.length-1){
            int reachable = 0;
            for(int i=0;i<=right;i++){
                reachable = Math.max(reachable, i+nums[i]);
            }
            left= right+1;
            right= reachable;
            jump++;
        }
        return jump;
    }

}