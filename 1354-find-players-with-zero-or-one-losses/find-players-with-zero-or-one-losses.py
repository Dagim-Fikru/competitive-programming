class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        notLost = []
        lostOne = []
        mapping = {}
        for i in range(len(matches)):
            mapping[matches[i][1]] = mapping.get(matches[i][1],0) + 1
        for i in range(len(matches)):
            if matches[i][0] not in mapping:
                notLost.append(matches[i][0])
        for key,value in mapping.items():
            if value==1:
                lostOne.append(key)
        notLost=list(set(notLost))
        lostOne=list(set(lostOne))
        lostOne.sort()
        notLost.sort()
        print(mapping)
        return [notLost,lostOne]
