class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        strOfNums = ""
        ans=[]
        for num in nums:
            strOfNums+=str(num)
        strOfNums = str(int(strOfNums)+1)
        for num in strOfNums:
            ans.append(int(num))
        return ans

        