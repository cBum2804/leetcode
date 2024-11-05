class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<Integer>[] bucket = new List[nums.length+1];
        Map<Integer, Integer> map= new HashMap<>();

        for(int i: nums){
            map.put(i, map.getOrDefault(i,0)+1);
        }
        for(int i: map.keySet()){
            int frequency = map.get(i);
            if(bucket[frequency]==null){
                bucket[frequency] = new ArrayList<>();
            }
            bucket[frequency].add(i);
        }

        int [] ans = new int[k];
        int counter =0;
        for(int i=bucket.length-1; i>=0 && counter<k; i--){
            if(bucket[i]!= null){
                for(int j: bucket[i] ){
                    ans[counter]= j;
                    counter ++;
                }
            }
        }

        return ans;
    }
}