class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count_right = Counter(nums)
        count_left = defaultdict(int)
        ans = {}
        for i in range(len(nums)):
            score = 0
            score+= count_right[1] + count_left[0]
            if nums[i]==0:
                count_left[nums[i]]+=1
            else:
                count_right[1]-=1
            ans[i]=score
        ans[i+1]=count_left[0]
        arr = []
        currElem = max(ans.values())
        for i,j in ans.items():
            if j==currElem:
                arr.append(i)
        return arr
        
            
