class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            if nums2.index(i)==len(nums2)-1:
                    ans.append(-1)
            else:
                j= nums2.index(i)+1
                while j<=len(nums2)-1:
                    if i<nums2[j]:
                        ans.append(nums2[j])
                        break
                    elif j==len(nums2)-1:
                        ans.append(-1)
                    j+=1
        return ans
            
        