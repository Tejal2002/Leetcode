class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

    #First , time = O(n logm) , m = size of the map
        # n = len(nums)
        # freq = {}

        # for i in range(n):
        #     freq[nums[i]] = freq.get(nums[i],0) + 1
        
        # for key in freq:
        #     if freq[key] == 1:
        #         return key
    
    #xor 
        xor  = 0
        for num in nums:
            xor ^= num
        
        return xor
