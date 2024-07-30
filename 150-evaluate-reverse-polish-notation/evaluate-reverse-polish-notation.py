class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for tk in tokens:
            if tk == '+':
                stack.append(stack.pop()+stack.pop())
            elif tk == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif tk == '*':
                stack.append(stack.pop()*stack.pop())
            elif tk == '/':
                a,b = stack.pop(), stack.pop()
                res = int(b/a) if a * b > 0 else -int(abs(b)/abs(a)) 
                stack.append(res)
            else:
                stack.append(int(tk))
        
        return stack[0]
