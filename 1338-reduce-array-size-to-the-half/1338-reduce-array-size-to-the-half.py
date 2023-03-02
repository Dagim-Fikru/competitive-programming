class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq= collections.Counter(arr)
        key = freq.values()
        newKey=sorted(key,reverse=True)
        # return freq
        atLeastHalf = len(arr)
        result = 0
        for i in newKey:
            atLeastHalf-= i
            result+=1
            if atLeastHalf <=len(arr)//2:
                return result
        return result
            