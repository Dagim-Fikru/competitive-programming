class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            elif stack[-1].isupper():
                if i.islower():
                    if stack[-1].lower()==i:
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
            else:
                if i.isupper():
                    if stack[-1].upper()==i:
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)

        return "".join(stack)

