class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        indxTonum = {}
        ans = []
        for i in range(len(mapping)):
            indxTonum[i]=mapping[i]
        for j in range(len(nums)):
            numToStr = list(str(nums[j]))
            # print(numToStr)
            for k in range(len(numToStr)):
                numToStr[k] = str(mapping[int(numToStr[k])])
            # print("".join(numToStr))
            ans.append(int("".join(numToStr)))
        res = defaultdict(list)
        for i in range(len(ans)):
            res[ans[i]].append(nums[i])
        # print(res)
        finalAns = []
        ans2 = list(set(ans))
        ans2.sort()
        for num in ans2:
            finalAns+=res[num]
        return finalAns