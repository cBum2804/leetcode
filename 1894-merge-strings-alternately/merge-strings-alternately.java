class Solution {
    public String mergeAlternately(String word1, String word2) {
        int w1=0;
        
        StringBuilder s = new StringBuilder();
        while(w1< word1.length() || w1< word2.length()){
            if(w1<word1.length()){
                s.append(word1.charAt(w1));
            }
            if(w1<word2.length()){
                s.append(word2.charAt(w1));
            }
            
            w1++;
        }

        
        return s.toString();
    }

}