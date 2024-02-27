class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(set(nums))
        frequency = {}
        l=0
        count=0
        for r in range(len(nums)):
            if nums[r] in frequency:
                frequency[nums[r]]+=1
            else:
                 frequency[nums[r]]=1
            while len(frequency)==n and l<=r:
                count+= len(nums)-r
                frequency[nums[l]]-=1
                if frequency[nums[l]]==0:
                    del frequency[nums[l]]
                l+=1
        return count
        # count=0
        # for i in range(len(nums)):
        #     check = set()
        #     for j in range(i,len(nums)):
        #         check.add(nums[j])
        #         if len(check)==n:
        #             count+=1
        # return count
