class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix_Y =[]
        prefix_N =[]
        countOfY = customers.count('Y')
        NumOfY=0
        NumofN=0
        for i in customers:
            if i=='Y':
                prefix_Y.append(countOfY-NumOfY+NumofN)
                NumOfY+=1
            if i=='N':
                prefix_Y.append(NumofN+countOfY-NumOfY)
                NumofN+=1
        prefix_Y.append(NumofN)
        return prefix_Y.index(min(prefix_Y))
        

        


