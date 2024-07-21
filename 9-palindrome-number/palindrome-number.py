class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
    #1st attempt
        # num_str = str(x)

        # rev_str = []

        # for i in range(len(num_str)-1,-1,-1):
        #     rev_str.append(num_str[i])
        

        # if num_str == ''.join(rev_str):
        #     return True
        # else:
        #     return False

    # #efficient

    #     num_str = str(x)
    #     return num_str == num_str[::-1]

    # WITHOUT CONVERTING INTO STRING

        sign = -1 if x < 0 else 1

        x = abs(x)
        og_num = x
        rev_num = 0

        while x != 0:
            digit = x % 10
            x = x // 10

            rev_num = rev_num * 10 + digit
        
        rev_num = rev_num * sign 

        if og_num == rev_num :
            return True  
        else:
            return False 

