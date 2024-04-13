class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # houses.sort()
        # heaters.sort()
        # ans = []
        # for house in houses:
        #     min_dist = float('inf')
        #     left = 0
        #     right = len(heaters)-1
        #     while left<=right:
        #         mid = (right+left)//2
        #         min_dist = min(min_dist,abs(house-heaters[mid]))
        #         if heaters[mid]==house:
        #             break
        #         elif heaters[mid]>house:
        #             right-=1
        #         else:
        #             left+=1
        #     ans.append(min_dist)
        # return max(ans)
        houses.sort()
        heaters.append(float('inf'))
        heaters.append(float('-inf'))
        heaters.sort()
        r=0
        i=0

        for house in houses:
            while heaters[i]<house:
                i+=1
            min_dist = min(abs(house-heaters[i]),abs(house-heaters[i-1]))
            r = max(r,min_dist)
        return r


