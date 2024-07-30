class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack = []
        # closing = {')':'(','}':"{",']':'['}

        # for lt in s:
        #     if lt in closing:
        #         if stack and stack[-1]==closing[lt]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(lt)
        
        # if not stack:
        #     return True

    # second
        
        stack = []
        closing = {')':'(','}':'{',']':'['}

        for brac in s :
            if brac in closing:
                if stack and stack[-1] == closing[brac]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brac)
        
        return not stack 
        
