class MyStack:

    def __init__(self):
        self.que1=[]
        # self.que2=[]
        

    def push(self, x: int) -> None:
        # while self.stack1:
        #     self.stack2.append(self.stack1.pop())
        self.que1.append(x)
        
        # while self.stack2:
        #     self.stack1.append(self.stack2.pop())
            
            
    def pop(self) -> int:
        return self.que1.pop()
        

    def top(self) -> int:
        return self.que1[-1]
        

    def empty(self) -> bool:
        if len(self.que1)==0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()