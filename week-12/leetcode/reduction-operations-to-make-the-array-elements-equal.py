class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        minArr = list(set(nums))
        minArr.sort(reverse=True)
        num_of_operation = 0
        for i in range(len(minArr)-1):
            num_of_operation+=frequency[minArr[i]]
            frequency[minArr[i+1]]+=frequency[minArr[i]]
        return num_of_operation