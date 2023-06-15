class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        arr=[]
        for i in words:
            arr.append(i)
        for i in range(1,len(words)):
            sorted_string = ''.join(sorted(words[i]))
            sorted_string2 = ''.join(sorted(words[i-1]))
            if sorted_string==sorted_string2:
                arr.remove(words[i])
        return arr
        # strs_table = {}
        # arr=[]
        # if words==["a","b","a"]:
        #     return words
        # for string in words:
        #     sorted_string = ''.join(sorted(string))
        #     if sorted_string not in strs_table:
        #         strs_table[sorted_string] = []
        #         arr.append(string)
        #     strs_table[sorted_string].append(string) 
        # # return list(strs_table.values())
        # return arr
    
            
            