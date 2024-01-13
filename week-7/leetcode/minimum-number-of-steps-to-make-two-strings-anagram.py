class Solution:
    def minSteps(self, s: str, t: str) -> int:
        CounterOfS = defaultdict(int)
        CounterOfT = defaultdict(int)
        for i in t:
            CounterOfT[i]+=1
        for i in s:
            CounterOfS[i]+=1
        count=0
        print(CounterOfT)
        print(CounterOfS)
        for char in CounterOfS:
            if CounterOfT[char]<CounterOfS[char]:
                count+=CounterOfS[char]-CounterOfT[char]
        return count




        