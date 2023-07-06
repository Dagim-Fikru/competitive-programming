class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        arr=[]
        i=0
        j=len(skill)-1
        while i<j:
            arr.append([skill[i],skill[j]])
            i+=1
            j-=1
        chemistry = arr[0][0] * arr[0][1]
        for i in range(1,len(arr)):
            if arr[0][0]+arr[0][1]==arr[i][0]+arr[i][1]:
                chemistry = chemistry + (arr[i][0] * arr[i][1])
            else:
                return -1
        return chemistry
            