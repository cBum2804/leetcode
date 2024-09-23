class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> count =new HashMap<>();
        Map.Entry<Integer, Integer> maxNum = null;
        for(int i=0;i<nums.length;i++){
            count.put(nums[i],count.getOrDefault(nums[i],0)+1);
        }

        for(Map.Entry<Integer, Integer> max: count.entrySet() ){
            if(maxNum==null || max.getValue().compareTo(maxNum.getValue())>0){
                maxNum = max;
            }
        }
        return maxNum.getKey();
       
    }
}