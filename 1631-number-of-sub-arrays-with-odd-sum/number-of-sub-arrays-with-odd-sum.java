class Solution {
    public int numOfSubarrays(int[] arr) {


        //brute force approach 
        // final int MOD = (int)(1e9 + 7);
        // int n = arr.length ;
        // int count = 0 ;

        // for(int startIndex =0 ; startIndex < n ; startIndex++)
        // {
        //     int currSum = 0;
        //     for(int endIndex = startIndex; endIndex < n ; endIndex++)
        //     {
        //         currSum += arr[endIndex];

        //         if(currSum % 2 != 0){
        //             count ++;
        //         }
        //     }
        // }

        // return count % MOD;

        
        //approach 2 
        int MOD = (int) Math.pow(10,9)+7;
        int n = arr.length ;
        
        //convert elements to 0(even), 1(odd)

        for(int i = 0; i < n; i++){
            arr[i] %= 2; // Convert elements to 0 (even) or 1 (odd)
        }

        int[] dpEven = new int[n],dpOdd = new int[n];

        //Initialization based on last element 
        if(arr[n-1]==0){
            dpEven[n-1] = 1;
        }else{
            dpOdd[n-1] = 1;
        }

        for(int num = n-2 ; num >=0 ; num--){

            if (arr[num] == 1) {
                // Odd element contributes to odd subarrays
                dpOdd[num] = (1 + dpEven[num + 1]) % MOD;
                // Even element continues the pattern
                dpEven[num] = dpOdd[num + 1];
            } else {
                // Even element contributes to even subarrays
                dpEven[num] = (1 + dpEven[num + 1]) % MOD;
                // Odd element continues the pattern
                dpOdd[num] = dpOdd[num + 1];
            }

        }

        int count = 0;
        for(int oddcount : dpOdd){
            count += oddcount;
            count %= MOD;
        }
        return count;
    }
}