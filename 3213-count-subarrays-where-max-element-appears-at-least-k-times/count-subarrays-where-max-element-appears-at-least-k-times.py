class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        num_of_subarrays = 0
        l = 0
        maxEl = max(nums)
        count = 0
        for r in range(len(nums)):
            if nums[r]==maxEl:
                count+=1
            while count>=k and r>=l:
                if nums[l]==maxEl:
                    count-=1
                l+=1
            num_of_subarrays+=r-l+1
        num_of_subarrays = ((n*(n+1))//2) - num_of_subarrays
        # print(count)
        return num_of_subarrays