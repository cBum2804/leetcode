function mergeAlternately(word1: string, word2: string): string {
let w1: number =0;
let output: string = "";
while(w1< word1.length || w1< word2.length){
    if(w1<word1.length){
        output = output.concat("",word1.charAt(w1));
    }
    if(w1< word2.length){
        output = output.concat("", word2.charAt(w1));
    }
    w1++;
}
return output;
};