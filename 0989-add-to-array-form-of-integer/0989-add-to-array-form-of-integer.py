class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        arr=[]
        x = int(''.join(str(i) for i in num))
        y=str(x+k)
        for i in y:
            arr.append(int(i))
        return arr
        
        