class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target = sum(nums)//2
        a = {0,nums[-1]}
        for i in range(len(nums)-2,-1,-1):
            b = set()
            for j in a:
                b.add(j + nums[i])
            a.update(b)
        if target in a:
            return True


        