function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
 let maxCandies: number =candies[0];
 let output: boolean[] = [];
 for(let i=0;i<=candies.length-1;i++){  
    if (candies[i]> maxCandies){
        maxCandies= candies[i];
    }
 }
 for(let i=0; i<=candies.length-1;i++){
    if(candies[i]+ extraCandies>= maxCandies){
        output.push(true);
    }
    else{
        output.push(false);
    }
 }
 return output;
};