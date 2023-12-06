class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i=0
        j=n
        arr=[]
        while j<len(nums):
            arr.append(nums[i])
            arr.append(nums[j])
            i+=1
            j+=1
        return arr