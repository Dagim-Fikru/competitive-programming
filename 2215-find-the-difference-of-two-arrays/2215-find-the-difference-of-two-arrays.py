class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr1=[]
        arr2=[]
        for i in nums1:
            if i not in nums2 and i not in arr1:
                arr1.append(i)
        for i in nums2:
            if i not in nums1 and i not in arr2:
                arr2.append(i)      
        return [arr1,arr2]