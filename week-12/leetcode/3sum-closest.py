class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        result = 0
        nums.sort()
        for i in range(len(nums)):
            j=i+1
            k= len(nums)-1
            while j<k:
                threeSum = nums[i]+nums[j]+nums[k]
                diff = abs(threeSum - target)
                if closest>=diff:
                    closest = diff
                    result = threeSum
                if threeSum>target:
                    k-=1
                elif threeSum<target:
                    j+=1
                else:
                    return threeSum
        return result