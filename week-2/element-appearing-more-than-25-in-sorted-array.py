class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        frequency = Counter(arr)

        for key,value in frequency.items():
            if value> len(arr)/4:
                return key