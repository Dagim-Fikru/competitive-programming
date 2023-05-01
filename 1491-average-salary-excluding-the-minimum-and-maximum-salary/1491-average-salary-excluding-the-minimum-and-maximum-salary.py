class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop(0)
        salary.pop(-1)
        x=0
        for i in range(len(salary)):
            x+=salary[i]
        return x/(i+1)
        # total=0
        # k=0
        # i=1
        # j=len(salary)-1
        # while i<j:
        #     total+=salary[i]
        #     k=i
        #     i+=1
        # return total/k
            
        