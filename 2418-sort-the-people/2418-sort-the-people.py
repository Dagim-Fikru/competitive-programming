class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr=[]
        my_dict = dict(zip(heights, names))
        heights.sort(reverse=True)
        # print(my_dict)
        for i in heights:
            arr.append(my_dict[i])
        return arr
        