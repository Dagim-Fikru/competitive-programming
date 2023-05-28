class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newList = list(((nums)))
        newList.sort()
        arr=[]
        HashMap = {}
        for i in range(len(newList)):
            if newList[i] not in HashMap:
                HashMap[newList[i]]=i
        for i in range(len(nums)):
            arr.append(HashMap[nums[i]])
        return arr
