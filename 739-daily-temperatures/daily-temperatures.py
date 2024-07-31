class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

    # brute force approach 
    #Time = O(n^2)  #time limit exceeded 

        # res = []
        
        # for i in range(len(temperatures)):
        #     count = 0
        #     for j in range(i+1 , len(temperatures)):
        #         if temperatures[i]<temperatures[j]:
        #             diff = j-i
        #             count += diff
        #             break
        #     res.append(count) 
        # return res

    # usin stack 
    #time = O(n) , space = O(n)

        res = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = (i-stackI)
            stack.append([t,i])
        
        return res
        
                

