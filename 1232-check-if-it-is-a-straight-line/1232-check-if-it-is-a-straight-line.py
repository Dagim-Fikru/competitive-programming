import numpy as np
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        for i in range(2,len(coordinates)):
            x2, y2 = coordinates[i-1]
            x3, y3 = coordinates[i]
            if (y1-y0)*(x3-x2)==(y3-y2)*(x1-x0):
                continue
            else:
                return False
        return True
        # if (x2 - x1)==0:
        #     initial_slope='a'
        # else:
        #     initial_slope = (y2 - y1) / (x2 - x1)
        # for i in range(2,len(coordinates)):
        #     slope=0
        #     x1, y1 = coordinates[i-1]
        #     x2, y2 = coordinates[i]
        #     if (x2 - x1)==0:
        #         slope=="a"
        #     else:
        #         slope = (y2 - y1) / (x2 - x1)
        #     if slope!=initial_slope:
        #         return False
        #     else:
        #         continue
        # return True
        # new_array=[]
        # if len(coordinates)==2:
        #     return True
        # x = np.array(coordinates)
        # a = x[0]
        # for i in range(1,len(coordinates)):
        #     c = np.cross(a, x[i])
        #     new_array.append((c))
        # new_array = np.array(new_array)
        # return new_array.all()