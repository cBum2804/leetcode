function threeSumClosest(nums: number[], target: number): number {
    nums.sort((a,b)=> a-b);
    let curr_sum: number = 0;
    let curr_diff: number = 0;
    let closest_sum: number = Number.POSITIVE_INFINITY;
    let min_diff: number = Number.POSITIVE_INFINITY;
    
    for(let i=0; i< nums.length -2; i++){
        let left: number = i+1, right:number= nums.length-1;

        while(left < right){
            curr_sum = nums[i]+ nums[left]+ nums[right];
            curr_diff = Math.abs(curr_sum-target);

            if(curr_diff < min_diff){
                min_diff = curr_diff;
                closest_sum = curr_sum;
            }
            if(curr_sum < target){
                left++;
            }
            else{
                right--;
            }

        }
    }
    return closest_sum;
};