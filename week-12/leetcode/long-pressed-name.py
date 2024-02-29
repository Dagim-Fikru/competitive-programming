class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i=0
        j=0
        if len(name)>len(typed) or name[0]!=typed[0]:
            return False
        while i<len(name) and j<len(typed):
            if name[i] == typed[j]:
                i+=1
            elif j>0 and typed[j-1] != typed[j]:
                return False
            j +=1
        while j<len(typed):
            if typed[j] != name[-1]:
                return False
            j+=1
        return i == len(name) and j == len(typed)
