function totalFruit(fruits: number[]): number {
    let start: number = 0;
    let fruit_map = new Map<number, number>();
    let output: number = 0;

    for(let end=0; end<=fruits.length-1; end++){
        fruit_map.set(fruits[end], (fruit_map.get(fruits[end]) || 0) + 1);

        while(fruit_map.size > 2){
            fruit_map.set(fruits[start], fruit_map.get(fruits[start])!-1);
            if(fruit_map.get(fruits[start])=== 0){
                fruit_map.delete(fruits[start]);
            }
            start++;
        }
        output = Math.max(output, end-start+1);
    }
    return output;
};