class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        l=0
        ans = 0
        r=0
        # if k==0:
        #     return 0
        while r<len(nums):
            product =product*nums[r]
            while product>=k and l<=r:
                product =product/nums[l]
                l+=1
            ans+=r-l+1
            r+=1
        return ans