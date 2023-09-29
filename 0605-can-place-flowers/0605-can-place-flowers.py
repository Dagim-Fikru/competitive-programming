class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        i=0
        while i<len(flowerbed):
            if flowerbed[i]==1:
                i+=2
            else:
                if i==len(flowerbed)-1:
                    count+=1
                    i+=1
                elif flowerbed[i+1]==0:
                    count+=1
                    i+=2
                else:
                    i+=1
        # print(i)
        # print(count)
        return n<=count
                
            
        # count = 0
        # if flowerbed[0]==1:
        #     for i in range(2,len(flowerbed),2):
        #         if flowerbed[i]==0:
        #             count+=1
        # else:
        #     for i in range(1,len(flowerbed),2):
        #         if flowerbed[i]==0:
        #             count+=1
        # return n==count
                