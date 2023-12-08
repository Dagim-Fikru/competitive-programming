class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater_than_pivot=[]
        less_than_pivot=[]
        equal = []
        for num in nums:
            if num<pivot:
                less_than_pivot.append(num)
            elif num==pivot:
                equal.append(num)
            else:
                greater_than_pivot.append(num)
        return less_than_pivot + equal + greater_than_pivot