class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeight = []
        for i in heights:
            sortedHeight.append(i)
        heights.sort()
        count=0
        # return sortedHeight
        for i in range(len(heights)):
            if heights[i]!=sortedHeight[i]:
                count+=1
            else:
                continue
        return count