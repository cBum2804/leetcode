function search(nums: number[], target: number): number {
    let start: number =0, end:number = nums.length-1;
    while(start<= end){
        let mid : number = Math.floor((start+end)/2);

        if(target=== nums[mid]){
            return mid;
        }
        if(nums[start]<= nums[mid]){
            if(nums[start]<= target && nums[mid]>= target){
                end = mid-1;
            }
            else{
                start= mid+1;
            }
        }
        else{
            if(nums[end]>= target && nums[mid]<=target){
                start= mid+1;
            }
            else{
                end = mid-1;
            }
        }
    }
    return -1
};