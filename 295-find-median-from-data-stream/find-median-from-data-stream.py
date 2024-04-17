class MedianFinder:

    def __init__(self):
        self.arr = []
    def addNum(self, num: int) -> None:
        self.arr.append(num)
    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr)%2==0:
            i= len(self.arr)//2
            self.median = (self.arr[i-1]+self.arr[i])/2
        else:
            i=len(self.arr)//2
            self.median = self.arr[i]
        return self.median
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()