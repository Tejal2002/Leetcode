class Solution {
    public boolean divideArray(int[] nums) {
        // Arrays.sort(nums);

        // for(int pos=0; pos<nums.length ; pos+=2)
        // {
        //     if(nums[pos] != nums[pos+1]){
        //         return false;
        //     }
        // }

        // return true;   


        //Hashmap approach
        Map<Integer, Integer> freq = new HashMap<>();

        for(int num: nums){
            freq.put(num,freq.getOrDefault(num,0) + 1);
        }

        for(int num: freq.keySet()){
            if(freq.get(num) % 2 != 0){
                return false;
            }
        }

        return true ;


    }
}