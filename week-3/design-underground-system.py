class UndergroundSystem:

    def __init__(self):
        self.HashTable1 = {}
        self.HashTable2= {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.HashTable1[id]= (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
    
        start, time = self.HashTable1[id]
        if (start,stationName) not in self.HashTable2:
            self.HashTable2[(start,stationName)]=[0,0]
        self.HashTable2[(start,stationName)][0]+=t-time
        self.HashTable2[(start,stationName)][1]+=1
        # self.HashTable2[id]=[stationName,t]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        total,count = self.HashTable2[(startStation,endStation)]
        # for i in range(len(self.HashTable1)):
        #     averageTime+= self.HashTable1[id][1]+ self.HashTable2[id][1]
        # averageTime = ()/2
        
        return total/count
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)