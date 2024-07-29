class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double avg;
        double ans;
        int sum = 0;
        for(int i=0;i<k;i++){
            sum+=nums[i];
        }
        avg = sum * 1.0/k;
        ans = avg;

        for(int i = k; i< nums.length;i++){
            sum+= nums[i]- nums[i-k];
            ans = Math.max(sum* 1.0/k,ans);
        }
        return ans;
    }
}