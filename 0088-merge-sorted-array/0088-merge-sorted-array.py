class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # while m>0:
        #     nums1.pop()
        #     m-=1
        # for i in range(n):
        #     nums1.append(nums2[i])
        # arr=[]
        # for i in range(m):
        #     arr.append(nums1[i])
        # for j in range(n):
        #     arr.append(nums2[j])
        # while nums1:
        #     nums1.pop()
        # while arr:
        #     nums1.append(arr.pop())
        # nums1.sort()
        x = len(nums1)-m
        while x>0:
            nums1.pop()
            x-=1
        # print(nums1)
        i=0
        j=0
        if len(nums1)==0:
            for i in nums2:
                nums1.append(i)
        else:
            while j<len(nums2):
                if i==len(nums1)-1 and nums1[i]<nums2[j]:
                    nums1.append(nums2[j])
                    j+=1
                elif nums1[i]<nums2[j]:
                    i+=1
                else:
                    nums1.insert(i,nums2[j])
                    j+=1
        # print(nums1)



