class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

    #first attempt 

        count = 0
        for i in range(len(nums)):

            if len(nums) > 1:
                if nums[i] != 0:
                    nums[count] = nums[i]
                    if count != i:
                        nums[i] = 0
                    count += 1
        
        return nums 
