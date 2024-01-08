class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        # for i in nums:
        #     if i==val:
        #         nums.pop(nums.index(i))
        #     else:
        #         continue
        print(nums)
        return len(nums)
                
        