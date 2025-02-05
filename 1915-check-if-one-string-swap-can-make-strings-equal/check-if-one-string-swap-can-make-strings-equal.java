class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        // If the strings are already equal, return true
        if (s1.equals(s2)) {
            return true;
        }

        // List to store the indices where s1 and s2 differ
        int first = -1, second = -1;
        int diffCount = 0;

        // Iterate through both strings to find differences
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                diffCount++;

                // Store first and second differing positions
                if (first == -1) {
                    first = i;
                } else if (second == -1) {
                    second = i;
                } else {
                    // More than 2 differences → return false
                    return false;
                }
            }
        }

        // Check if swapping characters at first and second makes them equal
        return (diffCount == 2 && 
                s1.charAt(first) == s2.charAt(second) && 
                s1.charAt(second) == s2.charAt(first));
    }
        
}
