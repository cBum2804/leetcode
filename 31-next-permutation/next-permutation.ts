/**
 Do not return anything, modify nums in-place instead.
 */
function nextPermutation(nums: number[]): void {
    let last :number, pointer: number;
    last = pointer = nums.length -1;
    let temp: number;
    while(last>0 && nums[last-1]>= nums[last]){
        last--;
    }
    if(last===0){
        nums.reverse();
        return;
    }
    let incr_pos: number = last-1;
    while(nums[pointer]<= nums[incr_pos]){
        pointer--;
    }
    temp = nums[incr_pos];
    nums[incr_pos] = nums[pointer];
    nums[pointer] = temp;
    let left:number= incr_pos+1, right:number = nums.length-1;

    while(left< right){
        temp =nums[left];
        nums[left] = nums[right];
        nums[right]= temp;
        left++; right--;
        
    }
};