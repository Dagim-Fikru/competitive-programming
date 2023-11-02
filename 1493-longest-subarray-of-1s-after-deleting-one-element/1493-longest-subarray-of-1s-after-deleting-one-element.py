class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        r,l = 0,0
        count=0
        maxLen = 0
        while r<len(nums):
            if nums[r]==0:
                count+=1
            while count>1:
                if nums[l]==0:
                    count-=1
                l+=1
                
            # if count1:
            #     if nums[l]==0:
            #         count-=1
            #     l+=1
            maxLen = max(maxLen,r-l+1)
            r+=1
        print(r,l)
        return maxLen-1
            
        # prev=0
        # count=0
        # ls=[]
        # visit=False
        # for i in nums:
        #     if i==0:
        #         visit=True
        #         ls.append(prev+count)
        #         prev=count
        #         count=0
        #     if i==1:
        #         count+=1
        # if not visit:
        #     count-=1
        # ls.append(count+prev)
        # return max(ls)
        