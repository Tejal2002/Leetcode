import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[][] mergeArrays(int[][] nums1, int[][] nums2) {
        int i = 0, j = 0;
        List<int[]> result = new ArrayList<>();  //Fixed capitalization

        while (i < nums1.length && j < nums2.length) {
            if (nums1[i][0] == nums2[j][0]) {  //Fixed indexing issue
                result.add(new int[]{nums1[i][0], nums1[i][1] + nums2[j][1]});
                i++;
                j++;
            } else if (nums1[i][0] < nums2[j][0]) {
                result.add(nums1[i]);  //Fixed incorrect single integer addition
                i++;
            } else {
                result.add(nums2[j]);  //Fixed incorrect single integer addition
                j++;
            }
        }

        //Add remaining elements from nums1
        while (i < nums1.length) {
            result.add(nums1[i]);
            i++;
        }

        //Add remaining elements from nums2
        while (j < nums2.length) {
            result.add(nums2[j]);  //Fixed incorrect variable usage
            j++;
        }

        return result.toArray(new int[result.size()][]);
    }
}
