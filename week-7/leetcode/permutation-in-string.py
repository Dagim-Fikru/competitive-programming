class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)
        counter2 = Counter(s2[:len(s1)])
        if counter1==counter2:
            return True
        for i in range(len(s2)-len(s1)):
            counter2[s2[i]]-=1
            counter2[s2[i+len(s1)]]=counter2.get(s2[i+len(s1)],0)+1
            if counter1==counter2:
                return True
        else:
            return False