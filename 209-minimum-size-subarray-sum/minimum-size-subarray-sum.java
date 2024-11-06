class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0; 
        int sum = 0;
        int result = Integer.MAX_VALUE;  // Start with an arbitrarily large number

        for (int right = 0; right < nums.length; right++) {
            sum += nums[right];

            // Shrink the window from the left while the sum is greater than or equal to the target
            while (sum >= target) {
                result = Math.min(result, right - left + 1); // Update the result with the current window size
                sum -= nums[left]; // Move the left pointer and subtract that value from sum
                left++;
            }
        }

        return (result == Integer.MAX_VALUE) ? 0 : result;  // Return 0 if no valid subarray was found
    }
}
