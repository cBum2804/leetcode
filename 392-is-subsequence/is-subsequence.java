class Solution {
    public boolean isSubsequence(String s, String t) {
        int sc = 0;
        int tc = 0;

        while (sc < s.length() && tc < t.length()) {
            if (s.charAt(sc) == t.charAt(tc)) {
                sc++;
            }
            tc++;
        }

        return sc == s.length();        
    }
}