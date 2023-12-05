class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr = []
        maxVal = max(candies)
        for i in candies:
            newVal=0
            newVal = i+extraCandies
            arr.append(maxVal<=newVal)
        return arr