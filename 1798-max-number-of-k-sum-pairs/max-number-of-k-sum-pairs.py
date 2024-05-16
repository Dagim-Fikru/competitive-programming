class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        ans=0
        while i<j:
            target = nums[i]+nums[j]
            if target>k:
                j-=1
            elif target<k:
                i+=1
            else:
                ans+=1
                i+=1
                j-=1
        return ans
