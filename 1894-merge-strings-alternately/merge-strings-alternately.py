class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ''
        for i in range(min(len(word1),len(word2))):
            result += word1[i] + word2[i]

        if len(word1) < len(word2):
            result += word2[len(word1):]
        else:
            result += word1[len(word2):]
        
        return result 

        #using list 
        