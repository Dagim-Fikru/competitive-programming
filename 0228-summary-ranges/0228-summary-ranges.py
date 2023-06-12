class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        arr = []
        if len(nums)==0:
            return arr
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    arr.append(f"{start}")
                else:
                    arr.append(f"{start}->{nums[i-1]}")
                start = nums[i]
        if start == nums[-1]:
            arr.append(str(start))
        else:
            arr.append(str(start) + "->" + str(nums[-1]))

        return arr
                
                
        