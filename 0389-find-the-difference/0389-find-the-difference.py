class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCount = Counter(s)
        tCount = Counter(t)
        for i in t:
            if sCount[i]==tCount[i]:
                continue
            else:
                return i
                
#         arr1= list(s)
#         arr2 = list(t)
#         while len(arr1)<len(arr2):
#             arr1.append(' ')
#         # hash_table = {}
#         # arr1.sort()
#         # arr2.sort()
#         # for i in range(len(arr2)):
#         #     if arr1[i]==arr2[i]
            
#         for i in range(len(arr2)):
#             if arr2[i] in arr1 or arr1[i]==" ":
#                 continue
#             else:
#                 return arr2[i]
            