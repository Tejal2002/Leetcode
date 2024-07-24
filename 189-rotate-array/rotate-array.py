class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
    #first appraoch
        # #incase k is greater than len(nums)
        # k = k % n

        # # new array
        # rotated = [0] * n

        # for i in range(n):
        #     rotated[(i+k) % n]= nums[i]
        
        # for i in range(n):
        #     nums[i]=rotated[i]

        # return nums

    #second approach

        nums.reverse()

        if k > len(nums):
            k = k % len(nums)

        #reverse the first k elemnts
        nums[:k] = reversed(nums[:k])

        #reverse next k elements
        nums[k:] = reversed(nums[k:])