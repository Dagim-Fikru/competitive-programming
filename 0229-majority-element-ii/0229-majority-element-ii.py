class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        setOfNums = set(nums)
        arr=[]
        for i in setOfNums:
            if nums.count(i)>len(nums)/3:
                arr.append(i)
        # for i in nums:
        #     if nums.count(i)>len(nums)/3:
        #         arr.append(i)
        # freq= collections.Counter(nums)
        # reverse_dict = {}
        # for key, value in freq.items():
        #     reverse_dict[value] = key
        # key = freq.values()
        # for i in key:
        #     if i>len(nums)/3:
        #         arr.append( reverse_dict[i])
        return arr
                
        