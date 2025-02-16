class Solution {
    public int[] constructDistancedSequence(int n) {
        int length = 2 * n - 1;
        int[] result = new int[length]; // Array to store the sequence
        boolean[] used = new boolean[n + 1]; // Tracks used numbers

        backtrack(result, used, n, 0);
        return result;
    }

    private boolean backtrack(int[] result, boolean[] used, int n, int index) {
        if (index == result.length) return true; // Successfully filled sequence

        if (result[index] != 0) // If already filled, move to next index
            return backtrack(result, used, n, index + 1);

        // Try placing numbers from n to 1 (largest first)
        for (int num = n; num >= 1; num--) {
            if (used[num]) continue; // Skip if already used

            // If num > 1, it must be placed at index and index + num
            if (num > 1 && (index + num >= result.length || result[index + num] != 0))
                continue; // If we can't place num at both required positions, skip

            // Place number
            result[index] = num;
            if (num > 1) result[index + num] = num;
            used[num] = true;

            // Recur to fill next number
            if (backtrack(result, used, n, index + 1)) return true;

            // Backtrack if placement didn't work
            result[index] = 0;
            if (num > 1) result[index + num] = 0;
            used[num] = false;
        }

        return false; // If no number could be placed, return false
    }
}
