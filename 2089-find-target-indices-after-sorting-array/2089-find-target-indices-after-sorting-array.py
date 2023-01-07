class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
            nums.sort()
            arr=[]
            if nums.count(target)==1:
                arr.append(nums.index(target))
            else:
                for i in range(nums.count(target)):
                    arr.append(nums.index(target)+i)
            return arr
        