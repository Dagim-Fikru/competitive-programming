class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer= [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            currentTemperature = temperatures[i]
            while stack and stack[-1][0] < currentTemperature:
                index = stack.pop()[1]
                answer[index] = i - index
            stack.append([currentTemperature, i])
        return answer
                
        # count=0
        # for i in range(len(temperatures)):
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[i]>=temperatures[j]:
        #             count+=1
        #             continue
        #         elif temperatures[i]<temperatures[j]:
        #             count+=1
        #             answer[i]=count
        #             count=0
        #             break
        # return answer
            
        
        