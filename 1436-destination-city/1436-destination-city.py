class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        arr=[]
        for i in range(len(paths)):
            if paths[i][0] not in arr:
                arr.append(paths[i][0])
        for i in range(len(paths)):
            if paths[i][1] not in arr:
                return paths[i][1]
        
        # newDict = {}
        # for i in range(len(paths)):
        #     if paths[i][0] in newDict.values():
        #         newDict 
            
        