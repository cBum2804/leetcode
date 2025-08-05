function numOfUnplacedFruits(fruits: number[], baskets: number[]): number {
    let output: number = 0;

    for(let fruit of fruits){
        let unplaced: number= 1;
        for(let i=0;i<=baskets.length-1; i++){
            if(fruit<= baskets[i]){
                unplaced= 0;
                baskets[i]=0;
                break;
            }
        }
        output= output+unplaced;
    }
    return output
};