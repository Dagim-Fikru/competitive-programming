import numpy as np
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        arr = []
        Count = Counter(deck)
        for key,value in Count.items():
            arr.append(value)
        check = np.array(arr)
        result = np.gcd.reduce(check)
        if result<=1:
            return False
        return True
        
        # if len(deck)<=1:
        #     return False
        # for key,indx in Count.items():
        #     if indx<check:
        #         if check%indx:
        #             return False
        #     else:
        #         if indx%check:
        #             return False
        # return True