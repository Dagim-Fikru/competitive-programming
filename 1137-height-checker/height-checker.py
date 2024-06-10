class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        sortedHeight = []
        for i in heights:
            sortedHeight.append(i)
        heights.sort()
        # return sortedHeight
        for i in range(len(heights)):
            if heights[i]!=sortedHeight[i]:
                count+=1
            else:
                continue
        return count