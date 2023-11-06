class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        mid =0
        if n%2==0:
            elmnts = int(n/2)
            mid = (nums[elmnts]+nums[elmnts])//2
            # mid = int(mid)
        else:
            mid = nums[n//2]
        # mid = mid//n
        print(mid)
        totalMove = 0
        for num in nums:
            totalMove+= abs(num-mid)
        return totalMove
            
#         maxEl = max(nums)
#         totalMove = 0
        
#         for num in nums:
#             totalMove+= maxEl-num
#         return totalMove
            
            