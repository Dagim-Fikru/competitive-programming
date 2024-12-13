class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        total = 0
        maxFreq = 0
        for key,value in freq.items():
            if value>maxFreq:
                total= value
                maxFreq = value
            elif value==maxFreq:
                total+=maxFreq
        print(freq)
        print(maxFreq)
        return total
