class Solution:
    def countElements(self, nums: List[int]) -> int:
        maxEl = max(nums)
        minEl = min(nums)
        freq = Counter(nums)
        if len(freq)==1:
            return 0
        return len(nums)-(freq[maxEl]+freq[minEl])