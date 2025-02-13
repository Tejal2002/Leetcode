class Solution {
    public int minOperations(int[] nums, int k) {

        PriorityQueue<Long> minHeap = new PriorityQueue<>();

        //add all the elements in the min heap
        for(int num : nums){
            minHeap.add((long)num);
        }

        int op = 0;

        while(minHeap.peek() < k && minHeap.size() > 1){

            // if(minHeap.size() < 2){
            //     return -1;
            // }

            long x = minHeap.poll();
            long y = minHeap.poll();

            long nVal = x*2 + y;

            minHeap.add(nVal);
            op++;
        }

        return (minHeap.peek()>=k ? op : -1);
        
    }
}