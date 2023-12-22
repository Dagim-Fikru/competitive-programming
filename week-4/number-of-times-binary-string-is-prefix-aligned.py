class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxFlip = 0
        count=0
        for i in range(len(flips)):
            maxIndex = i+1
            maxFlip = max(maxFlip,flips[i])
            if maxFlip==maxIndex:
                count+=1
        return count