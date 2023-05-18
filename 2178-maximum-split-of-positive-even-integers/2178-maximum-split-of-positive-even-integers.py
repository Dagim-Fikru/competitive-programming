class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        i=2
        arr=[]
        if finalSum%i!=0:
            return []
        newSum=0
        while newSum<finalSum:
            newSum+=i
            arr.append(i)
            i+=2
            # if newSum%2==0:
            #     finalSum = newSum
            #     arr.append(i)
            #     i+=2
            # # else:
            # #     i+=2
        if newSum==finalSum:
            return arr
        else:
            arr.remove(newSum-finalSum)
        return arr