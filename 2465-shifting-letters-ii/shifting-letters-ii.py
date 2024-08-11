class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # shiffting = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        #i know i can use ord but lets findout first
        listOfs = list(s)
        arr = [0]*(len(s)+1)
        for i,j,k in shifts:
            if k==0:
                arr[i]-=1
                arr[j+1]+=1
            else:
                arr[i]+=1
                arr[j+1]-=1
        # print(arr)
        presum=[]
        sum=0
        for i in arr:
            sum+=i
            presum.append(sum)
        for i in range(len(listOfs)):
            listOfs[i]=chr(ord("a") + ((ord(s[i]) + presum[i]) - ord("a"))%26)
        # print(listOfs) 

            
            
        # for i in range(len(shifts)):
        #     for j in range(shifts[i][0],shifts[i][1]+1):
        #         if shifts[i][2]==0:
        #             if listOfs[j]=='a':
        #                 listOfs[j]='z'
        #             else:
        #                 listOfs[j]=shiffting[shiffting.index(listOfs[j])-1]
        #         else:
        #             if listOfs[j]=='z':
        #                 listOfs[j]='a'
        #             else:
        #                 listOfs[j]=shiffting[shiffting.index(listOfs[j])+1]
        return "".join(listOfs)
                
        