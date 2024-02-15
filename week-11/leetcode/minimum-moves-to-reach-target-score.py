class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        step = 0
        while target>1:
            if target%2 and maxDoubles!=0:
                target-=1
                step+=1
            elif target%2 and maxDoubles==0:
                step+=target-1
                break
            else:
                if maxDoubles>0:
                    target//=2
                    step+=1
                    maxDoubles-=1
                else:
                    target-=1
                    step+=1
        return step