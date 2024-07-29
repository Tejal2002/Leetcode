class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, cnt = 0, 0, 0
        while right < len(nums):
            if nums[right] == 0:
                cnt += 1
            right += 1
            if cnt > 1:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
        return right - left - 1