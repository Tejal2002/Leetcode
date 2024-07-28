class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #using hashset 

        numSet = set(nums)
        longest = 0

        for n in nums:
            #check for the start of sequence
            length = 0
            if (n-1) not in numSet:
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest 
                
