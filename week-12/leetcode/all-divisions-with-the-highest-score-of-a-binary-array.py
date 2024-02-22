class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        count_right = Counter(nums)
        count_left = defaultdict(int)
        ans = []
        for i in range(len(nums)):
            score = 0
            score+= count_right[1] + count_left[0]
            if nums[i]==0:
                count_left[nums[i]]+=1
            else:
                count_right[1]-=1
            ans.append([score,i])
        ans.append([count_left[0],i+1])
        ans.sort(reverse=True)
        arr = []
        currElem = ans[0][0]
        for i,j in ans:
            if i==currElem:
                arr.append(j)
        return arr
        
            
