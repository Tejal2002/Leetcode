class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

      
        # write_index = 1
        # for i in range(1,len(nums)):
        #     if nums[i] != nums[i-1]:
        #         nums[write_index] = nums[i]
        #         write_index += 1 
        
        # return write_index

        count = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
        
        return count
        


             
        