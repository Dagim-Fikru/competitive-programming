class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []
        
    def pushFront(self, val: int) -> None:
        # if len(self.queue)<self.size:
        self.queue.insert(0, val)
            
        
    def pushMiddle(self, val: int) -> None:
        self.queue.insert(len(self.queue)//2, val)
        

    def pushBack(self, val: int) -> None:
        self.queue.append(val)
        
        
    def popFront(self) -> int:
        if len(self.queue)==0:
            return -1
        else:
            backElement = self.queue[0]
            self.queue.remove(backElement)
            return backElement
        

    def popMiddle(self) -> int:
        if len(self.queue)==0:
            return -1
        # arr = []
        else:
            if len(self.queue)<=2:
                middleElement=self.queue[0]
            else:
                if len(self.queue)%2!=0:
                    middleElement = self.queue[(len(self.queue)//2)]
                else:
                    middleElement = self.queue[(len(self.queue)//2)-1]   
            # arr.append(middleElement)
            self.queue.remove(middleElement)
            return middleElement
        

    def popBack(self) -> int:
        if len(self.queue)==0:
            return -1
        else:
            backElement = self.queue[len(self.queue)-1]
            self.queue.remove(backElement)
            return backElement
                
#         if len(self.queue)==0:
#             return -1
#         backElement = self.queue[0]
#         self.queue.remove(self.queue[0])
#         return backElement
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()