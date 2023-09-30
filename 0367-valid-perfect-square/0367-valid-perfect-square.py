class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<0:
            return False
        if num==1 or num==0:
            return True
        left=0
        right= num//2
        while left<=right:
            mid = (left+right)//2
            perfsq = mid**2
            if perfsq==num:
                return True
            elif perfsq<num:
                left = mid+1
            else:
                right=mid-1
        return False
        # i = 1
        # while i*i <= num:
        #     if i*i == num:
        #         return True
        #     i += 1
        # return False
        
        