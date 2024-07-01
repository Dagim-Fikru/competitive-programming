class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        n = len(arr)
        for i in range(n):
            if arr[i]%2:
                count+=1
                if count==3:
                    break
            else:
                count=0
        return count==3