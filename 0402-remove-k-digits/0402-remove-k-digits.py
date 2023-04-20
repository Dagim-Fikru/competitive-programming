class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # arr= list(map(int,num))
        stack = []
        for digit in num:
            while k > 0 and len(stack) > 0 and stack[-1] > digit:
                k -= 1
                stack.pop()  
            stack.append(digit)
        if k > 0:
            stack = stack[:-k]     
        return "".join(stack).lstrip("0") or "0"
#         count=0
#         i = 0
#         if len(num)==1:
#             return "0"
#         elif len(set(num))==1:
#             while k>0:
#                 arr.pop()
#                 k-=1
#         while i<=len(arr)-2:
#             if arr[i]>arr[i+1]:
#                 arr.pop(i)
#                 count+=1
#             elif arr[i]<arr[i+1]:
#                 arr.pop(i+1)
#                 count+=1
#             else:
#                 i+=1
#             if k==count:
#                 break
            
#         my_string = ''.join(str(i) for i in arr)
#         my_string=int(my_string)
#         return str(my_string)
            
            
        
        
        