class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = skill[0]*skill[-1]
        target = skill[0] + skill[-1]
        i=1
        j=len(skill)-2
        while i<j:
            if skill[i]+skill[j]!=target:
                return -1
            chemistry+=skill[i]*skill[j]
            i+=1
            j-=1
        return chemistry
            