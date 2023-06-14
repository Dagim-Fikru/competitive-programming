class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_table = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in strs_table:
                strs_table[sorted_string] = []
            strs_table[sorted_string].append(string) 
        return list(strs_table.values())
        # for i in range(len(strs)):
        #     arr=[]
        #     arr.append(strs[i])
        #     for j in range(len(strs)):
        #         if i==j:
        #             continue
        #         if len(strs[i])==len(strs[j]):
        #             result = all(char in strs[i] and strs[i].count(char)==strs[j].count(char) for char in strs[j])
        #             if result==True:
        #                 arr.append(strs[j])
        #     arr.sort()
        #     if arr not in newHash:
        #         newHash.append(arr)
        # return newHash