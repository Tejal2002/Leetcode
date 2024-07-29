class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = r = 0
        ans = 0
        cnt = 0
        n = len(nums)
        while r < n:
            if nums[r] == 0:
                cnt += 1
            while cnt > k:
                if nums[l] == 0:
                    cnt -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans