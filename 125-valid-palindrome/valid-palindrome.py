class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        #uses in built functions 
        #time = o(n) , space - o(n)

        # normal = "".join(char.lower() for char in s if char.isalnum())

        # return normal == normal[::-1]

        #using 2 pointer method 
        #time = O(n) , space = o(1)
        
        l, r = 0, len(s)-1
        while l<r :
            while l<r and not self.alpha_num(s[l]):
                l += 1
            while r>l and not self.alpha_num(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1 , r-1
        return True


    def alpha_num(self,c):
        return (ord('A') <=ord(c)<=ord('Z')) or (ord('a')<=ord(c)<=ord('z')) or (ord('0')<=ord(c)<=ord('9'))



        

