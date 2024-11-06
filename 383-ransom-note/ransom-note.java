class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        
        Map<Character, Integer> maga = new HashMap<>();

        for(int i=0; i< magazine.length(); i++){
            maga.put(magazine.charAt(i), maga.getOrDefault(magazine.charAt(i),0)+1);
        }

        for(int i=0; i< ransomNote.length(); i++){
            if(!maga.containsKey(ransomNote.charAt(i)) || maga.get(ransomNote.charAt(i))<=0){
                return false;
            }
            maga.put(ransomNote.charAt(i), maga.get(ransomNote.charAt(i))-1);
        }
        return true;
    }
}