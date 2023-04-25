class SmallestInfiniteSet:

    def __init__(self):
        self.stack=list(range(1,1001))
        

    def popSmallest(self) -> int:
        return self.stack.pop(self.stack.index(min(self.stack)))

    def addBack(self, num: int) -> None:
        if num not in self.stack:
            self.stack.append(num)
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)