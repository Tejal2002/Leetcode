class Solution {
    public int maxAscendingSum(int[] nums) {

        int currsum = nums[0];
        int maxsum = 0;
        for(int i=1 ; i < nums.length ; i++){
            if (nums[i-1] < nums[i]){
                currsum += nums[i];
            }
            else{
                maxsum = Math.max(currsum, maxsum);
                currsum = nums[i];
            }
        }   
        return Math.max(currsum,maxsum);     
    }
}