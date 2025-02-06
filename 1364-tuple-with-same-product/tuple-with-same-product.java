class Solution {
    public int tupleSameProduct(int[] nums) {
        Map<Integer, Integer> productCount = new HashMap<>();
        int count = 0;

        // Count pairs (a, b) that produce the same product
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int product = nums[i] * nums[j];
                productCount.put(product, productCount.getOrDefault(product, 0) + 1);
            }
        }

        // Compute the number of valid tuples
        for (int freq : productCount.values()) {
            if (freq > 1) {
                count += freq * (freq - 1) * 4; // Each pair contributes 4 valid tuples
            }
        }

        return count;
    }
}