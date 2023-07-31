# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,u = 0,n
        result = 0
        while l<=u:
            mid = (l+u)//2
            if isBadVersion(mid)==True:
                result = mid
                u=mid-1
            else:
                l=mid+1
        return result
                
        