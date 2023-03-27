class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack1=[]
        n=len(s)
        i=0
        while (i<n):
            if s[i]!=')':
                stack1.append(s[i])
            else:
                stack2=[]
                while (stack1[-1]!='('):
                    stack2.append(stack1.pop())
                stack1.pop()
                stack1.extend(stack2)
            i+=1

        return "".join(stack1)
        
        