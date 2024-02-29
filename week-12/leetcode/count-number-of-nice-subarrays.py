class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = []
        for i in range(len(nums)):
            if nums[i]%2:
                nums[i]=1
            else:
                nums[i]=0
        total = 0
        for i in range(len(nums)):
            total+=nums[i]
            prefix.append(total)
        n = len(prefix)
        freq = Counter(prefix)
        count=0
        count+=prefix.count(k)
        prefix = list(set(prefix))
        i=0
        j=1
        while j<len(prefix):
            diff = prefix[j]-prefix[i]
            if diff>k:
                i+=1
            elif diff<k:
                j+=1
            else:
                count+= freq[prefix[i]]*freq[prefix[j]]
                i+=1
                j+=1
        return count

