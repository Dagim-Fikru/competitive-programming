class Solution:
    def smallestNumber(self, num: int) -> int:
        strinOfNum = str(num)
        arr = []
        for i in strinOfNum:
            if i=='-':
                continue
            else:
                arr.append(int(i))
        if num>0:
            arr.sort()
            if arr[0]!=0:
                newNum = "".join(map(str, arr))
                return int(newNum)
            else:
                i=0
                j=1
                while j<len(arr) and arr[j]==0:
                    j+=1
                arr[i],arr[j]= arr[j],arr[i]
                newNum = "".join(map(str, arr))
                return int(newNum)
        else:
            arr.sort(reverse=True)
            arr2 = str(arr)
            newNum = "".join(map(str, arr))
            return -int(newNum)



        
        