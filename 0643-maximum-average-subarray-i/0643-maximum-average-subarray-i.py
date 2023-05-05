class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumOf = sum(nums[:k])
        avarage = sumOf/k
        
        for i in range(1,len(nums)-k+1):
            sumOf = sumOf - nums[i-1]
            sumOf = sumOf + nums[i+k-1]
            newAv = sumOf/k
            avarage = max(newAv,avarage)
        return avarage