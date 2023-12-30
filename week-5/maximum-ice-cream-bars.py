class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count=0
        maxElem = max(costs)
        count_arr = [0]*(maxElem+1)
        for i in range(len(costs)):
            count_arr[costs[i]]+=1
        outputArr = []
        for i in range(len(count_arr)):
            while count_arr[i]>0:
                outputArr.append(i)
                count_arr[i]-=1
        for i in outputArr:
            if coins>=i:
                count+=1
                coins-=i
            else:
                break
        return count
            
        