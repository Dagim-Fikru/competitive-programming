class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = Deque(nums)
        x.rotate(k)
        while nums:
            nums.pop()
        nums.extend(x)
        
              