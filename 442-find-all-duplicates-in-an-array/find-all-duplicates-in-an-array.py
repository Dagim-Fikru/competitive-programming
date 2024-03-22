class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]<0:
                ans.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
        return ans
        # check = set()
        # arr= []
        # for num in nums:
        #     if num in check:
        #         arr.append(num)
        #     else:
        #         check.add(num)
        # return arr