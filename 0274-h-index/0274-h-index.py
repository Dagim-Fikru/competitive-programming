class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count=0
        citations.sort(reverse=True)
        i=0
        # j=len(citations)-1
        while i<=len(citations)-1:
            if citations[i]>=i+1:
                count+=1
            else:
                break
            i+=1
        return count