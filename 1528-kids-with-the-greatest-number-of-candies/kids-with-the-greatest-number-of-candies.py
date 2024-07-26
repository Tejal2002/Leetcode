class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
    #first 
        result  = []

        for i in range(len(candies)):
            flag = 1
            total = candies[i] + extraCandies
            for j in range(len(candies)):
                if total < candies[j]:
                    flag = 0
            
            if flag == 0:
                result.append(False)
            else:
                result.append(True)
            
        return result  

    #Second
        # result = []
        # max_candy = max(candies)

        # for i in range(len(candies)):
        #     if candies[i] + extraCandies >= max_candy:
        #         result.append(True)
        #     else:
        #         result.append(False)
            
        # return result