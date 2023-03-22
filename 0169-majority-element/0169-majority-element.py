class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        freq= collections.Counter(nums)
        reverse_dict = {}
        for key, value in freq.items():
            reverse_dict[value] = key
        key = freq.values()
        for i in key:
            if i>n/2:
                return(reverse_dict[i])
        # print(freq)
        # print(reverse_dict)
        # for i in nums:
        #     if nums.count(i)>n/2:
        #         return i
        