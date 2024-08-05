class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        for i in arr:
            if count[i]>1:
                continue
            else:
                k-=1
                if k==0:
                    return i
        return ""
                