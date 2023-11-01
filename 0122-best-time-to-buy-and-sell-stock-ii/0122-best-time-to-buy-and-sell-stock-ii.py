class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr=[]
        i=0
        j=1
        
        while j<len(prices):
            if prices[i]<prices[j]:
                arr.append(prices[j]-prices[i])
                i+=1
            else:
                i=j
            j+=1
        # arr.sort()
        return sum(arr)
                