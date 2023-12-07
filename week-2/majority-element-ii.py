class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # setOfNums = set(nums)
        n=len(nums)
        freq = Counter(nums)
        arr=[]
        for i in freq:
            if freq[i]>n/3:
                arr.append(i)
        # for i in setOfNums:
        #     if nums.count(i)>len(nums)/3:
        #         arr.append(i)
        return arr
                
        