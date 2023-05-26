class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        arr=[]
        s2=""
        for key, value in counter.items():
            arr.append([key,value])
        sorted_list = sorted(arr, key=lambda x: -x[1])
        for i in range(len(arr)):
            while sorted_list[i][1]>0:
                s2+=sorted_list[i][0]
                sorted_list[i][1]-=1
        return s2
        