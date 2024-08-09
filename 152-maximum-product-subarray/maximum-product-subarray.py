class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = max(nums)
        currmax , currmin = 1 , 1

        for n in nums:
            if n == 0:
                currmax , currmin = 1, 1
            tmp = currmax #because we r updating it in next line
            currmax = max(n*currmax, n*currmin , n)
            currmin = min(n*tmp, n*currmin , n)
            res = max(res , currmax)
        
        return res 
