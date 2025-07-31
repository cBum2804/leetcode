function merge(intervals: number[][]): number[][] {
    intervals.sort((a,b)=> a[0]-b[0]);
    let output:number[][] = [];

    for (let interval of intervals){
        if(output.length===0 || output[output.length-1][1]< interval[0]){
            output.push(interval);
        }
        else{
            output[output.length-1] = [output[output.length-1][0],Math.max(output[output.length-1][1], interval[1])];
        }
    
    }
    return output;
};