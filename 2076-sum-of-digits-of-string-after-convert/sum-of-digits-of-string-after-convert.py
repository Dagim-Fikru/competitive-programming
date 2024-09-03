class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = ""
        res = 0
        for char in s:
            ans+=str(ord(char)-ord('a') + 1)
        while k:
            for i in ans:
                res+=int(i)
            k-=1
            ans = str(res)
            res = 0
        return int(ans)