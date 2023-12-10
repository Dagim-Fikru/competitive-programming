class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mapping = {}
        for i in range(len(nums)):
            mapping[nums[i]]=i
        for i in range(len(operations)):
            nums[mapping[operations[i][0]]]= operations[i][1]
            mapping[operations[i][1]]= mapping[operations[i][0]]
        return nums