class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        word = s.split()

        rev_words = word[::-1]

        rev_string = ' '.join(rev_words)

        return rev_string