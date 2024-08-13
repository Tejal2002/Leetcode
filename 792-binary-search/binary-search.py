class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    
    # first , time = log(n)
        # l, r = 0 , len(nums)-1

        # while l<=r :
        #     m = (l+r)//2

        #     if nums[m] < target :
        #         l = m+1
        #     elif nums[m] > target :
        #         r = m-1
        #     else:
        #         return m 
        
        # return -1

    #2nd time (Iterative solution)
        low , high = 0 , len(nums) - 1

        while low <= high :
            mid  = (low + high) // 2

            if nums[mid] == target :
                return mid 
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1

