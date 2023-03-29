class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]*=0
            else:
                continue
        for i in nums:
            if i==0:
                arr.append(i)
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(i)
        # nums.sort(reverse=True)
        # for i in nums:
        #     if i==0:
        #         nums.remove(nums[i])
                
            # if nums[i]==0:
            #     arr.append(nums[i])
            #     nums.remove(nums[i])
            # if i==0:
            #     arr.append(i)
            #     nums.remove(i)
        # for i in arr:
        #     nums.append(i)
        return nums
        