class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]!="*":
                stack.append(s[i])
            else:
                stack.pop()
                # s.replace('',s[i])
        return "".join(stack)
                
        # arr = list(s)
        # for i in range(len(s)):
        #     if arr[i]!='*':
        #         continue
        #     else:
        #         arr.pop(i-1)
        #         arr.pop(i)
        # return "".join(arr)
        