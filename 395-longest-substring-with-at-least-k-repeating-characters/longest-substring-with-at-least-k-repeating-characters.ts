function longestSubstring(s: string, k: number): number {
    if(s.length< k){
        return 0;
    }
    let charFreq : {[key: string]: number}= {};
    for(let char of s){
        if(!(char in charFreq)){
            charFreq[char] = 1;
        } else{
            charFreq[char]++;
        }
    }
    for(let i =0; i<s.length; i++){
        let char = s[i];

        if (charFreq[char]< k){
            let left = longestSubstring(s.slice(0, i), k);
            let right = longestSubstring(s.slice(i + 1), k);
            return Math.max(left, right);
        }
    }
    return s.length;
};