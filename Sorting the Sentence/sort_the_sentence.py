class Solution:
    def sortSentence(self, s: str) -> str:
        x=s.split()
        y=[None] * len(x)
        for i in x:
            for k in i:
                for j in range(1,len(x)+1):
                    if k==str(j):
                        w=i.strip(str(j))
                        y[j-1]=w
        return " ".join(y)
