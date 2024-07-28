class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        res, d = 0, Counter(nums)
        for val1, val1_cnt in d.items():
            val2 = k - val1
            # to get rid of duplicates consider only pairs where val1 >= val2
            if val1 < val2 or val2 not in d: continue 
            res += min(val1_cnt, d[val2]) if val1 != val2 else val1_cnt//2
        
        return res