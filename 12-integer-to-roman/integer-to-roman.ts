function intToRoman(num: number): string {
    let numList=  [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    let symbolList = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];

    let result = "";

    for(let i=0; i< numList.length; i++){
        while(num>= numList[i]){
            result+= symbolList[i];
            num-=numList[i];
        }
    } 
    return result;
};