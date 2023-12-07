class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        arr=[]
        minSum = float('inf')
        indexToElement1 = {}
        indexToElement2 = {}
        for index,item in enumerate(list1):
            indexToElement1[item]=index
        for index,item in enumerate(list2):
            indexToElement2[item]=index
        for word in list1:
            if word in indexToElement2:
                if indexToElement1[word] + indexToElement2[word]==minSum:
                    arr.append(word)
                    minSum = min(minSum,indexToElement1[word] + indexToElement2[word])
                elif indexToElement1[word] + indexToElement2[word]<minSum:
                    while arr:
                        arr.pop()
                    arr.append(word)
                    minSum = min(minSum,indexToElement1[word] + indexToElement2[word])
        return arr

                
