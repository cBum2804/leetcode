class Solution {
    public int findShortestSubArray(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        HashMap<Integer, Integer> first_seen= new HashMap<>();
        int degree = 0;
        int min_len = 0;

        for(int i=0;i<nums.length;i++){
            first_seen.putIfAbsent(nums[i], i);
            map.put(nums[i],map.getOrDefault(nums[i],0)+1);
            if(map.get(nums[i])> degree){
                degree = map.get(nums[i]);
                min_len = i - first_seen.get(nums[i]) + 1;
            }
            else if(degree == map.get(nums[i])){
                min_len=Math.min(min_len,i-first_seen.get(nums[i])+1);
            }
        }
        return min_len;

    }
}