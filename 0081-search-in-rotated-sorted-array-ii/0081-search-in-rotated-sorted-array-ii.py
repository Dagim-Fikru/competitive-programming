class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Setofnums = set(nums)
        # for i in Setofnums:
        #     if i==target:
        #         return True
        # return False
        i=0
        j=len(nums)-1
        while i<=j:
            if nums[i]==target or nums[j]==target:
                return True
            i+=1
            j-=1
        return False