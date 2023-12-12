class OrderedStream:

    def __init__(self, n: int):
        self.arr= [None]*(n+1)
        self.ptr =0
    def insert(self, idKey: int, value: str) -> List[str]:
        self.ans = []
        self.arr[idKey-1] = value
        while self.arr[self.ptr]!=None and self.ptr<len(self.arr)-1:
            self.ans.append(self.arr[self.ptr])
            self.ptr+=1
        # print(self.arr)
        return self.ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)