class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        if len(nums)<4:
            return res
        nums.sort()

        for i in range(len(nums)-3):
            if i >0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left,right=j+1,len(nums)-1
                while left<right:
                    cursum=nums[i]+nums[j]+nums[left]+nums[right]
                    if cursum==target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
                    if cursum<target:
                        #to enlarge the numbers
                        left+=1
                    if cursum>target:
                        right-=1
        return res