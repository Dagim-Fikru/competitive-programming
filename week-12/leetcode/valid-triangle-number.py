class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        num_of_triangles = 0
        for i in range(2,len(nums)):
            j=0
            k=i-1
            while k>j:
                if nums[j]+nums[k]>nums[i]:
                    num_of_triangles+=k-j
                    k-=1
                else:
                    j+=1
        return num_of_triangles
        