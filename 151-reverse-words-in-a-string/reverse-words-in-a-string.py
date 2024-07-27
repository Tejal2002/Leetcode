class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Time = O(N)

        # word = s.split()
        # rev_words = word[::-1]
        # rev_string = ' '.join(rev_words)
        # return rev_string

        # Optimal using array 

        i=0
        length = len(s)
        word_pos = []  #to store start and end indices of words 

        while i<length:
            
            #skip leading spaces , vvvimp
            while i<length and s[i] == ' ':
                i += 1
            if i == length:
                break
            start = i

            while i<length and s[i] != ' ':
                i += 1
            end = i-1

            word_pos.append((start, end))
        
        result = []

        for start, end in reversed(word_pos):
            word = s[start:end+1]
            result.append(word)

        return ' '.join(result)