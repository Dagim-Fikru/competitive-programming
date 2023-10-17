class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.append(bottom-1)
        special.append(top+1)
        special.sort()
        diff = 0
        for i,j in zip(special,special[1:]):
            diff = max(diff,j-i-1)
        print(i,j)
        return diff
        
        
                
            
        
#         for i in special:
#             if i in arr:
#                 arr.pop(arr.index(i))
#         if arr==[]:
#             return 0
#         conc = 0
#         print(arr)
#         i=0
#         j=i+1
#         first = arr[0]
#         while j<len(arr):
#             if arr[i]+1==arr[j]:
#                 i+=1
#                 j+=1
#             elif arr[i]+1!=arr[j]:
#                 diff = arr[j-1]-first
#                 conc= max(diff,conc)
#                 i=i+1
#                 j=j+1
#                 first = arr[i]
#             elif j==len(arr)-1:
#                 diff = arr[j]-first
#                 conc= max(diff,conc)
                
#         return conc
                
                
#         i=0
#         j=i+1
#         while j<len(arr):
#             diff=0
#             if arr[i] not in special and arr[j] not in special:
#                 j+=1
#             elif arr[j] in special:
#                 diff= arr[j]-arr[i]
#                 i=j+1
#                 j=i+1
#                 conc = max(conc,diff)
#             elif j==len(arr)-1:
#                 diff= arr[j]-arr[i]+1
#                 i=j+1
#                 j=i+1
#                 conc = max(conc,diff)
                
#         return conc
                
                
                