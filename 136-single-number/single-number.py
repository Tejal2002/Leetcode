class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

    #First
        n = len(nums)
        freq = {}

        for i in range(n):
            freq[nums[i]] = freq.get(nums[i],0) + 1
        
        for key in freq:
            if freq[key] == 1:
                return key
        