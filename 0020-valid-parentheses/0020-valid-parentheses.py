class Solution:
    def isValid(self, s: str) -> bool:
        isYes= False
        stackOfChar = []
        # stackOfChar[0]=j
        for i in s:
            # if len(stackOfChar)==0:
            if i=='(' or i=='[' or i=='{':
                stackOfChar.append(i)
                # else:
                #     break
            else:
                if len(stackOfChar)!=0:
                    if i==')':
                        if stackOfChar[-1]=='(':
                            stackOfChar.pop()
                            isYes=True
                        else:
                            isYes=False
                            break
                    elif i==']':
                        if stackOfChar[-1]=='[':
                            stackOfChar.pop()
                            isYes=True
                        else:
                            isYes=False
                            break
                    elif i=='}':
                        if stackOfChar[-1]=='{':
                            stackOfChar.pop()
                            isYes=True
                        else:
                            isYes=False
                            break
                # elif len(stackOfChar)==1:
                #     isYes=False
                else:
                    isYes = False
                    break
        if len(stackOfChar)!=0:
            isYes=False
                        
            # if len(stackOfChar)==0 and (i==')' or i==']' or i=='}'):
                # isYes = False
                # break
                
        return isYes
        
        
        