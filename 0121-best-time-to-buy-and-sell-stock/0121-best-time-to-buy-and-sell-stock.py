class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxStok = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         stok = prices[j]-prices[i]
        #         maxStok = max(stok,maxStok)
        # return maxStok
        i=0
        j=1
        maxStok = 0
        while j<len(prices):
            if prices[i]<prices[j]:
                maxStok = max(maxStok,prices[j]-prices[i])
            else:
                i=j
            j+=1
        return maxStok