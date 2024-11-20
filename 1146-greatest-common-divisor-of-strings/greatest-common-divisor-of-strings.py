class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""
        if str1+str2==str2+str1:
            for char in str1+str2:
                if len(ans)!=math.gcd(len(str1),len(str2)):
                    ans+=char
                else:
                    break
        return ans
            