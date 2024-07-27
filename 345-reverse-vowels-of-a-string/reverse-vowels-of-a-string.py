class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        word  = list(s)
        start = 0
        end = len(word)-1
        vowels = "aeiouAEIOU"

        while start < end:

        #traverse start forward till it finds vowel
            while start<end and vowels.find(word[start])==-1:
                start += 1

        #traverse end back till it finds vowel 
            while start<end and vowels.find(word[end])==-1:
                end -= 1

        #swap strart and end position vowels 
            word[start],word[end] = word[end], word[start]

        #move pointers for next interations
            start += 1
            end -= 1

        return ''.join(word)

