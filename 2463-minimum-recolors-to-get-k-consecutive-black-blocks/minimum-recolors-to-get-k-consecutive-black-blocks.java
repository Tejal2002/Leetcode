class Solution {
    public int minimumRecolors(String blocks, int k) {

        // Sliding window appraoch 
        int left = 0, numWhites = 0 , numRecolors = Integer.MAX_VALUE;

        for(int right=0; right<blocks.length();right++){

            //increment num whites 
            if(blocks.charAt(right)=='W'){
                numWhites++;
            }

            // when right reaches the value of k 
            if(right-left+1 == k){
                numRecolors = Math.min(numRecolors, numWhites);

                if(blocks.charAt(left)=='W'){
                    numWhites -- ;
                }

                left++;


            }
        }

        return numRecolors;
        
    }
}