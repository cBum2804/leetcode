function longestConsecutive(nums: number[]): number {
    if(nums.length === 0){
        return 0;
    }
    let maxLength: number=0;
    let numSet: Set<number>= new Set(nums);

    for(let i of numSet){
        if (!(numSet.has(i-1))){
            let current: number = i;
            let count: number =1;

            while(numSet.has(current+1)){
                count ++;
                current++;
                
            }
            maxLength = Math.max(maxLength, count);
        }
    }
    return maxLength;
};