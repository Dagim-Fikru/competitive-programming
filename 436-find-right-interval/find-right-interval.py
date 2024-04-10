class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        arr = sorted((num[0], i) for i, num in enumerate(intervals))
        ans = []
        for num in intervals:
            low, high = 0, len(arr) - 1
            target = num[1]
            index = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid][0] >= target:
                    index = arr[mid][1]
                    high = mid - 1
                else:
                    low = mid + 1
            ans.append(index)
        return ans
