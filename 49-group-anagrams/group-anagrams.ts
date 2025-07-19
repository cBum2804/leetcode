function groupAnagrams(strs: string[]): string[][] {
    let myList = new Map<string, string[]>();
    for(let word of strs){
        let sortedStrs = word.split('').sort().join('');
        if(!myList.has(sortedStrs)){
            myList.set(sortedStrs, [word]);
        }
        else{
        
            myList.get(sortedStrs)!.push(word);
        }
    }
    return Array.from(myList.values());
};