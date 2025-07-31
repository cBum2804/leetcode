function singleNumber(nums: number[]): number {
    if(nums.length===1){
        return nums[0];
    }
    let numSet = new Set<number>();
    for (let num of nums){
        if (numSet.has(num)){
            numSet.delete(num)
        }
        else{
            numSet.add(num)
        }
    }
    let output:number[] = [...numSet];
    return output[0];
};