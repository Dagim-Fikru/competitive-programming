class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        comp = float('-inf')
        stack = []
        for i in range(n-1,-1,-1):
            if nums[i] > comp:
                while stack and stack[-1] < nums[i]:
                    comp = stack.pop()
                stack.append(nums[i])
            elif nums[i] < comp:
                return True
        return False
        