class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n =len(nums)
        count = 0

    # Count how many times the current element is greater than the next element
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1

    # If more than one such point is found, it can't be a rotated sorted array
        if count > 1:
            return False

        return True
