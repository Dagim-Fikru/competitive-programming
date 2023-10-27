class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        maxStok = 0
        while j<len(prices):
            if prices[i]<prices[j]:
                stok = prices[j]-prices[i]
                maxStok = max(maxStok,stok)
            else:
                i=j
            j+=1
        return maxStok