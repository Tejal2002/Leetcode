import java.util.*;

class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        List<Integer> less = new ArrayList<>();
        List<Integer> equal = new ArrayList<>();
        List<Integer> greater = new ArrayList<>();

        // Categorizing elements
        for (int num : nums) {
            if (num < pivot) {
                less.add(num);
            } else if (num == pivot) {
                equal.add(num);
            } else {
                greater.add(num);
            }
        }

        // Merging all lists into a single array
        int[] result = new int[nums.length];
        int index = 0;
        
        // Adding elements less than pivot
        for (int num : less) {
            result[index++] = num;
        }
        
        // Adding elements equal to pivot
        for (int num : equal) {
            result[index++] = num;
        }
        
        // Adding elements greater than pivot
        for (int num : greater) {
            result[index++] = num;
        }

        return result;
    }
}
