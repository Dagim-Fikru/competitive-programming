class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxNum = 0
        sub = s[:k]
        subStr = defaultdict(int)
        for j in sub:
            subStr[j]+=1
        result = subStr['a'] + subStr['e'] + subStr['i'] + subStr['o']+subStr['u']
        maxNum = max(maxNum,result)
        for i in range(len(s)-k):
            subStr[s[i]]-=1
            subStr[s[i+k]]+=1
            result = subStr['a'] + subStr['e'] + subStr['i'] + subStr['o']+subStr['u']
            maxNum = max(maxNum,result)
        return maxNum
        
        