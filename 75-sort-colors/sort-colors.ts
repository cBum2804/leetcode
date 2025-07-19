/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
    let low: number=0, mid: number = 0, high:number = nums.length-1;
    while (mid<= high){
        if(nums[mid] === 0){
            let temp = nums[low];
            nums[low] = nums[mid];
           nums[mid]= temp;
            low++; mid++;
        }
        else if(nums[mid]===1 ){
            mid++;
        }
        else{
            let temp2 = nums[high];
            nums[high] =nums[mid];
            nums[mid] = temp2;
            high --;
            
        }
    }
};