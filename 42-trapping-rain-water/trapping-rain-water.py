class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        #Two pointer method
        #time = O(n) , space = o(1)

        l,r = 0, len(height)-1
        maxLeft , maxRight = height[l], height[r]
        res = 0

        while l<r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft,height[l])
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight,height[r])
                res += maxRight - height[r]
        return res