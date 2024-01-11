class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        check = {}
        l=0
        maxFruit = 0 
        for r in range(len(fruits)):
            check[fruits[r]]= check.get(fruits[r],0) + 1
            while len(check)>2:
                if check[fruits[l]]==1:
                    del check[fruits[l]]
                else:
                    check[fruits[l]]-=1
                l+=1
            maxFruit = max(maxFruit,r-l+1)
        return maxFruit
        
        
        