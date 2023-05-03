class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
        # arr=[]
        # for i in nums1:
        #     if i in nums2 and i not in arr:
        #         arr.append(i)
        # return arr