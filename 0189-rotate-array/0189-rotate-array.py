class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # arr=[]
        # while k>=1:
        #     arr.append(nums.pop())
        #     k-=1
        # arr2 = arr[:]
        # for i in range(len(arr)):
        #     nums.insert(i,arr2.pop())
        # while arr:
        #     nums.append(arr.pop())
        # if len(nums)<=2:
        #     pass
        # else:
        #     arr=[]
        #     i=0
        #     j=len(nums)-k
        #     while i<len(nums)-k:
        #         if j<=len(nums)-1:
        #             arr.append(nums[j])
        #             j+=1
        #         else:
        #             arr.append(nums[i])
        #             i+=1
        #     while nums:
        #         nums.pop()
        #     nums.extend(arr)
        x = Deque(nums)
        x.rotate(k)
        while nums:
            nums.pop()
        nums.extend(x)
        
              