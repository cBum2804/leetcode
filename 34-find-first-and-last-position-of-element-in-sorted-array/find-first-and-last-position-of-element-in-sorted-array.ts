function searchRange(nums: number[], target: number): number[] {
    function binarySearch(nums: number[], target: number, is_left: boolean= true): number{
        let left:number = 0, right:number = nums.length-1, index:number =-1;

        while(left<=right){
            let mid:number= Math.floor((left+right)/2);
            if(nums[mid]> target){
                right = mid-1;
            }
            else if(nums[mid]< target){
                left = mid+1;
            }
            else{
                index = mid;
                if(is_left){
                    right= mid-1;
                }
                else{
                    left= mid+1;
                }
            }
        }
        return index;    
    }
    let left = binarySearch(nums, target, true);
    let right = binarySearch(nums, target, false);
    return [left, right];
    
};