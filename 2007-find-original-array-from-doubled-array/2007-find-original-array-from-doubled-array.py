class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        arr = []
        if len(changed)%2!=0:
            return arr
        
        dic = Counter(changed)
        changed.sort()
        for i in changed:
            if i == 0 and dic[i] >=2:
                arr.append(i)
                dic[i]=dic[i]-2
            elif i>0 and dic[i] and dic[i*2]:
                arr.append(i)
                dic[i] -=1
                dic[i*2] -=1
        
        if len(arr) == len(changed)//2:
            return arr
        else:
            return []