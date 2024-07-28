class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
    
    #brute force approach but doesnt work 
    #time = O(n^2)

    #     res = 0

    #     for l in range(len(height)):
    #         for r in range(l+1,len(height)):
    #             area = (r-l) * min(height[l], height[r])
    #             res = max(res,area)
        
    #     return res

    #Optimal solution using two pointers 

        l, r = 0 , len(height)-1
        res = 0

        while l<r :
            area = (r-l) * min(height[l], height[r])
            res = max(res,area)

            if height[l]<height[r]:
                l+=1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
        
        return res
            



