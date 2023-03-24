class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack1=[]
        for i in tokens:
            if i=='+':
                stack1.append(stack1.pop()+stack1.pop())
            elif i=='-':
                stack1.append(-(stack1.pop()-stack1.pop()))
                
            elif i=='*':
                stack1.append(stack1.pop()*stack1.pop())
                
            elif i=='/':
                x,y = stack1.pop(),stack1.pop()
                stack1.append(int((y/x)))
            else:
                stack1.append(int(i))
        return stack1[0]
            
        
        