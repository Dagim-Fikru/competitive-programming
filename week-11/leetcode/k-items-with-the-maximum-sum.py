class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        maxPoss = 0
        while k>0:
            if numOnes!=0:
                maxPoss+=1
                numOnes-=1
            else:
                if numZeros!=0:
                    numZeros-=1
                else:
                    maxPoss-=1
                    numNegOnes-=1
            k-=1
        return maxPoss

        