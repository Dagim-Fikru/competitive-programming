class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        first =0
        second =0
        merege =[]
        while first<len(firstList) and second<len(secondList):
            temp =[]
            if firstList[first][1] >= secondList[second][0] and firstList[first][0] <= secondList[second][1]:
                f = max(firstList[first][0],secondList[second][0])
                s = min(secondList[second][1],firstList[first][1])
                temp.append(f)
                temp.append(s) 
                merege.append(temp.copy())
                if s == secondList[second][1]:
                    second +=1
                else:
                    first +=1
            elif firstList[first][0] <= secondList[second][1] and firstList[first][1] >= secondList[second][0]:
                f = max(firstList[first][0],secondList[second][0])
                s = min(secondList[second][1],firstList[first][1])
                temp.append(f)
                temp.append(s) 
                merege.append(temp.copy())
                if s == secondList[second][1]:
                    second +=1
                else:
                    first +=1
            else:
                if firstList[first][0] < secondList[second][0]:
                    first +=1
                else:
                    second +=1
        return merege