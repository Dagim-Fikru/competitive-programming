class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr=[]
        pos = 0
        neg = 0
        while pos<len(nums) or neg<len(nums):
            if pos<=len(nums)-1:
                if nums[pos]>0:
                    if len(arr)==0:
                        arr.append(nums[pos])
                        pos+=1
                    elif arr[-1]<0:
                        arr.append(nums[pos])
                        pos+=1
                elif nums[pos]<0:
                    pos+=1
            if neg<=len(nums)-1:
                if nums[neg]<0:
                    if len(arr)==0:
                        pass
                    else:
                        if arr[-1]>0:
                            arr.append(nums[neg])
                            neg+=1
                elif nums[neg]>0:
                    neg+=1
        return arr
