class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count=0
        nums.sort()
        for i in nums:
            if i<0:
                count+=1
            elif i==0:
                return 0
            else:
                break
        if count%2==0:
            return 1
        return -1
        
        # product=1
        # for i in nums:
        #     product*=i
        # if product>0:
        #     return 1
        # elif product<0:
        #     return -1
        # return 0
        