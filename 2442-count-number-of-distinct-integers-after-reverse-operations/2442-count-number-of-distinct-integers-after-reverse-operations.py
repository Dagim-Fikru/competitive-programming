class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        setOfNum = set(nums)
        setOfRev=set()
        # setOfNum.add(2)
        for i in setOfNum:
            j=str(i)
            # j=int(j[::-1])
            # print(j)
            setOfRev.add(int(j[::-1]))
        finalSet=setOfNum.union(setOfRev)
        return(len(finalSet))
        
        