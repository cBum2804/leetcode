function maximumGap(nums: number[]): number {
    let maxDiff: number= 0;
    if(nums.length<2){
        return 0;
    }
    nums.sort((a,b)=> a-b);
    if(nums.length===2){
        return nums[1]- nums[0];
    }
    for(let i=0;i<nums.length-1;i++){
        if(nums[i+1]-nums[i] > maxDiff){
            maxDiff = nums[i+1]-nums[i];
        }
    }
    return maxDiff;
};