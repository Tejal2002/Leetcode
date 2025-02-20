class Solution {
    public String findDifferentBinaryString(String[] nums) {
        int n = nums.length;
        StringBuilder res = new StringBuilder();
        
        // Construct the unique binary string by flipping the diagonal bits
        for (int i = 0; i < n; i++) {
            res.append(nums[i].charAt(i) == '0' ? '1' : '0');
        }
        
        return res.toString();
    }
}
