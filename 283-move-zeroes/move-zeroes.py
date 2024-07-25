class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

    #first attempt 

        # count = 0
        # for i in range(len(nums)):

        #     if len(nums) > 1:
        #         if nums[i] != 0:
        #             nums[count] = nums[i]
        #             if count != i:
        #                 nums[i] = 0
        #             count += 1
        # return nums 

    #second attempt
        # count = 0

        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[count] = nums[i]
        #         count += 1
        
        # for i in range(count,len(nums)):
        #     nums[i] = 0

    # 2 pointer approach 

        j = -1

        for i in range(len(nums)):
            if nums[i]==0:
                j = i
                break
        
        # if  no zero found 
        if j == -1:
            return nums

        for i in range(j+1,len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums
            

            
