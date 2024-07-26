class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd_str(a,b):
            while b:
                a, b = b, a%b
            return a
        
        if str1 + str2 != str2 + str1:
            return ""
        else:
            gcd_len = gcd_str(len(str1), len(str2))
            return str2[:gcd_len]
        
        