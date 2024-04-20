from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = SortedList([])
        ans = []

        for i in range(len(nums)-1,-1,-1):
            indx = arr.bisect_left( nums[i])
            ans.append(indx)
            arr.add(nums[i])
        return ans[::-1]