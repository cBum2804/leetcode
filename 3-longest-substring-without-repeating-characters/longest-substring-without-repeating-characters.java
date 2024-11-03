class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> mapSet = new HashMap<>();
        int left = 0;
        int maxLength = 0;

        for(int right = 0; right< s.length(); right++){
            if(mapSet.containsKey(s.charAt(right))){
                left = Math.max(left, mapSet.get(s.charAt(right))+1);
            }
            mapSet.put(s.charAt(right), right);
            maxLength = Math.max(maxLength, right -left + 1);
        }
        return maxLength;
    }
}