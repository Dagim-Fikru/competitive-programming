class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        for i in range(len(s)):
            if s[i]!= '#':
                stack1.append(s[i])
            else:
                if len(stack1)==0:
                    continue
                stack1.pop()
        for i in range(len(t)):
            if t[i]!= '#':
                stack2.append(t[i])
            else:
                if len(stack2)==0:
                    continue
                stack2.pop()
        return stack1==stack2
        
        
        