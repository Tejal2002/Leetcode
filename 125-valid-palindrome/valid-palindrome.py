class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        normal = "".join(char.lower() for char in s if char.isalnum())

        return normal == normal[::-1]
