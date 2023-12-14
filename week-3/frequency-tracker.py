class FrequencyTracker:

    def __init__(self):
        self.hsmap = defaultdict(int)
        self.freq = defaultdict(int)
    def add(self, number: int) -> None:
        self.freq[self.hsmap[number]]-=1
        self.hsmap[number]+=1
        self.freq[self.hsmap[number]]+=1
    def deleteOne(self, number: int) -> None:
        self.freq[self.hsmap[number]]-=1
        self.hsmap[number]-=1
        self.freq[self.hsmap[number]]+=1
        if self.hsmap[number]<0:
            del (self.hsmap[number])
    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency]


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)