class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(n,0,-1)]
        while len(arr)>1:
            i=0
            while k-1>i:
                arr.insert(0,arr.pop())
                i+=1
            arr.pop()
        return arr[0]
        

            
        