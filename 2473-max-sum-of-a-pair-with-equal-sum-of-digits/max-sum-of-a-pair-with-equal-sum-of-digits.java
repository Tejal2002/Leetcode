class Solution {
    public int maximumSum(int[] nums) {

        Map<Integer,Integer> digitSumMap = new HashMap<>();
        int maxSum = -1;

        for(int num : nums){
            int dSum = digitSum(num);

            if (digitSumMap.containsKey(dSum)){
                maxSum = Math.max(maxSum , num + digitSumMap.get(dSum));
            }
            digitSumMap.put(dSum, Math.max(digitSumMap.getOrDefault(dSum, 0), num) );
        }

        return maxSum ;
        
    }

    private int digitSum(int num){
        int sum = 0;
        while(num>0){
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}