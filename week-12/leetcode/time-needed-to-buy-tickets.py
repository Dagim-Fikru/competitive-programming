class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        timeTaken = 0
        while tickets[k]>0:
            for j in range(len(tickets)):
                if tickets[j]==0:
                    continue
                else:
                    tickets[j]-=1
                    timeTaken+=1
                if j==k and tickets[j]==0:
                    break
        return timeTaken


