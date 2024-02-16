class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequency = Counter(arr)
        sorted_arr = sorted(arr, key=lambda x: (frequency[x], x), reverse=True)
        while k:
             sorted_arr.pop()
             k-=1
        return len(set(sorted_arr))
