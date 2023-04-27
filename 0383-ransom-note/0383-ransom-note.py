class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr1= list(ransomNote)
        arr2=list(magazine)
        for i in arr1:
            if i in arr2 and arr1.count(i)<=arr2.count(i):
                continue
            else:
                return False
        return True
        
        # for i in ransomNote:
        #     if i in magazine:
        #         continue
        #     else:
        #         return False
        # return True