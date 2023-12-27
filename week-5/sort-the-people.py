class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr=[]
        my_dict = dict(zip(heights, names))
        # heights.sort(reverse=True)
        for i in range(len(heights)):
            for j in range(len(heights)-i-1):
                if heights[j]>heights[j+1]:
                    heights[j],heights[j+1] = heights[j+1],heights[j]
        # print(my_dict)
        for k in range(len(heights)-1,-1,-1):
            arr.append(my_dict[heights[k]])
        # print(heights)
        return arr
        