class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        total=0
        k=0
        i=1
        j=len(salary)-1
        while i<j:
            total+=salary[i]
            k=i
            i+=1
        return total/k
            
        