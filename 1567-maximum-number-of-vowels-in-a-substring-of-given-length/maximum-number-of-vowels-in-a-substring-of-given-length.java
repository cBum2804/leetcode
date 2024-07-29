class Solution {
    public int maxVowels(String s, int k) {
        
        int count = 0;

        for(int i=0;i<k;i++){
           char ch = s.charAt(i);
            if(isVowel(ch)){
                count++;
            }
        }
        int ans = count;
        for(int i=k;i<s.length();i++){
           char chari = s.charAt(i);
           char charmi= s.charAt(i-k);

            if(isVowel(chari)){
                count++;
            }

            if(isVowel(charmi)){
                count--;
            }
            ans = Math.max(count, ans);

        }

       return ans;

    }
    public boolean isVowel(char ch){
        if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'){
            return true;
        }
        else{
            return false;
        }
       }
}