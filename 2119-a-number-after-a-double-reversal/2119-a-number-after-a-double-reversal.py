class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        strOfNums = str(num)
        rev1 = strOfNums[::-1]
        rev1=int(rev1)
        rev2 = str(rev1)[::-1]
        return int(rev2)==num
        