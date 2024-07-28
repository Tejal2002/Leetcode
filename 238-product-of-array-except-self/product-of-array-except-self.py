class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
 
        #1st attempt
        # result =[]
        
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             product *= nums[j]
        #     result.append(product)
        
        # return result
        
        #2nd attempt for O(n)
        # result = []
        # pre = 1
        # post = 1

        # for num in nums:
        #     result.append(pre)
        #     pre *= num              #1,1,2,6
        
        # for i in range(len(nums)-1,-1,-1):
        #     result[i] *= post
        #     post *= nums[i] 
        
        # return(result)

        # Third 

        result = []
        pre = 1
        post = 1

        for num in nums:
            result.append(pre)
            pre *= num

        for i in range(len(nums)-1,-1,-1):
            result[i] *= post
            post *= nums[i]

        return result 