class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left, right = 1, x
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
                result = mid
            else:
                right = mid - 1

        return result
        # range1 = range(0,(x//2)+1)
        # if x == 0 or x == 1:
        #     return x
        # if x%2==0:
        #     arr= [i for i in range1 if i % 2 == 0]
        # # else:
        # #     arr=[i for i in range1 if i % 2 != 0]
        # l, u = 0, len(arr)-1
        # while l<=u:
        #     mid = (u+l)//2
        #     if arr[mid]*arr[mid]==x:
        #         return arr[mid]
        #     elif arr[mid]*arr[mid]>x:
        #         u=mid-1
        #     else:
        #         l=mid+1
        # return arr[l-1]
            
            
        