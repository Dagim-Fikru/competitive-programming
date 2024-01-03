class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=0
        j=0
        minCommon = float('inf')
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                minCommon = min(minCommon,nums1[i])
                i+=1
                j+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                i+=1
        if minCommon!=float('inf'):
            return minCommon
        return -1