class OrderedStream:

    def __init__(self, n: int):
        self.arr= []
        self.ptr =1
    def insert(self, idKey: int, value: str) -> List[str]:
        self.ans = []
        self.arr.append([idKey,value])
        self.arr.sort()
        for i in range(len(self.arr)):
            if self.arr[i][0]== self.ptr:
                self.ans.append(self.arr[i][1])
                self.ptr+=1
        return self.ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)