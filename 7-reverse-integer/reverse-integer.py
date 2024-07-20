class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

    #1st attempt 
        #Handle negative numbers
        # negative = False

        # if x<0:
        #     negative = True
        #     x = -x

        # str_num = str(x)
        # rev_str=[]
        
        # for i in range(len(str_num)-1,-1,-1):
        #     rev_str.append(str_num[i])
        
        # rev_num = int(''.join(rev_str))

        # if negative:
        #     rev_num = -rev_num

        # if rev_num<-2**31 or rev_num>2**31 -1:
        #     return 0
        # else:
        #     return rev_num
    
    #2nd attempt by not converting into sring 
        rev_num = 0

        sign = -1 if x < 0 else 1
        x = abs(x)    #very very imp step
        
        while x != 0:
            digit = x % 10
            x = x // 10

            rev_num = rev_num*10 + digit

        if rev_num<-2**31 or rev_num>2**31 -1:
            return 0
        else:
            return sign*rev_num
           
        

