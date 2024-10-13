class Solution {
    public int hIndex(int[] citations) {
         Arrays.sort(citations);
        int n = citations.length;
        for (int i = 0; i < n; i++) {
            // Check if the number of papers with citations >= citations[i] is greater or equal to citations[i]
            if (citations[i] >= n - i) {
                return n - i;
            }
        }
        return 0;
    }
}