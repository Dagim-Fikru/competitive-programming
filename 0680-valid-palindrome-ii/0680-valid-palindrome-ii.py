class Solution:
    def validPalindrome(self, s: str) -> bool:
        d=0
        # isYes = False
        arr=list(s)
        i=0
        j=len(arr)-1
        while i<=j:
            if arr[i]!=arr[j]:
                arr2=arr[:i] + arr[i+1:]
                arr3=arr[:j] + arr[j+1:]
                # if arr2==arr2[::-1] or arr3==arr3[::-1]:
                #     isYes = True
                return arr2==arr2[::-1] or arr3==arr3[::-1]
            i+=1
            j-=1
        return True
        # while i<j:
        #     if arr==arr[::-1]:
        #         isYes=True
        #         break
        #     x=arr[i]
        #     arr.pop(i)
        #     if arr==arr[::-1]:
        #         isYes = True
        #         break
        #     else:
        #         arr.insert(i,x)
        #         y=arr[j]
        #         arr.pop(j)
        #         if arr==arr[::-1]:
        #             isYes = True
        #             break
        #         else:
        #             arr.insert(j,y)
        #     i+=1
        #     j-=1
        # return isYes
                
                
                
        
        