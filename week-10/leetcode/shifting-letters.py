class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shiffting = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        prefixSum = []
        arr = list(s)
        preSum = 0
        for i in shifts:
            preSum+=i
            prefixSum.append(preSum)
        for i in range(len(arr)):
            if i==0:
                arr[i]= chr(ord("a") + ((ord(s[i]) + prefixSum[-1]) - ord("a"))%26)
            else:
                arr[i]=chr (ord("a") + ((ord(s[i]) + (prefixSum[-1]-(prefixSum[i-1]))) - ord("a"))%26)
        return "".join(arr)