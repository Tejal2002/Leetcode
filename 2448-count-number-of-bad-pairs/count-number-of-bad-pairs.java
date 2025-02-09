class Solution {
    public long countBadPairs(int[] nums) {
        int n = nums.length;
        long totalPairs = (long) n * (n - 1) / 2; // Total possible pairs (i, j) where i < j
        
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        long goodPairs = 0;
        
        for (int j = 0; j < n; j++) {
            int key = nums[j] - j; // Transform the condition to nums[j] - j == nums[i] - i
            
            if (freqMap.containsKey(key)) {
                goodPairs += freqMap.get(key); // Count good pairs
            }
            
            freqMap.put(key, freqMap.getOrDefault(key, 0) + 1);
        }
        
        return totalPairs - goodPairs; // Bad pairs = total pairs - good pairs
    }
        
}