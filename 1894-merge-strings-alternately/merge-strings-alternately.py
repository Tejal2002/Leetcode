class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # result = ''
        # for i in range(min(len(word1),len(word2))):
        #     result += word1[i] + word2[i]

        # if len(word1) < len(word2):
        #     result += word2[len(word1):]
        # else:
        #     result += word1[len(word2):]
        
        # return result 

        #using list 
        result = []

        l1 = len(word1)
        l2 = len(word2)

        for i in range(min(l1, l2)):
            result.append(word1[i])
            result.append(word2[i])
        
        if l1 < l2:
            result.append(word2[l1:])
        else:
            result.append(word1[l2:])

        return "".join(result)