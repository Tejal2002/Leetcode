class Solution {
    public int longestNiceSubarray(int[] nums) {
        int i = 0;
        int j = 0;

        int result = 1;
        int mask = 0;
        int n = nums.length;

        while(j<n){
            while((mask & nums[j]) != 0){ //keep shrinking the window 
                mask ^= nums[i];
                i++;
            }
            result = Math.max(result, j-i+1);
            mask |= nums[j];
            j++;
        }

        return result;

        
    }
}