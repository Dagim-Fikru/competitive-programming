class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=0
        dic={}
        for i in nums:
            target = k-i
            if target in dic and dic[target]>0:
                count+=1
                dic[target]-=1
            else:
                if i not in dic:
                    dic[i]=0
                dic[i]+=1
        return count
                    
        # num_counts = Counter(nums)
        # for num in num_counts:
        #     if k-num in num_counts:
        #         if k-num == num:
        #             count += (num_counts[num] // 2)
        #         else:
        #             count += min(num_counts[num], num_counts[k-num])
        # return abs(count-2)