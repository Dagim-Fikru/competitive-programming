class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mapp = {}
        for i in nums:
            if i in mapp:
                mapp[i]+=1
            else:
                mapp[i]=1
        for key,value in mapp.items():
            if value>=2:
                return key