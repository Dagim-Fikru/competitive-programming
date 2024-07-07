class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles+(numBottles-1)//(numExchange-1)
        #  n + (n - 1) / (x - 1)