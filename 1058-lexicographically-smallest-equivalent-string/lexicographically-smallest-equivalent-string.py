class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        d=dict()
        for letter in range(ord('a'), ord('z')+1):
            d[chr(letter)]=chr(letter)
        
        def find(p):
            if p!=d[p]:
                d[p]=find(d[p])
                return d[p]
            return p
        
        def union(x,y):
            if d[x]==y:
                return 

            if y<d[x]:
                if d[x]!=x:
                    union(d[x],y)
                d[x]=y
            else:
                union(y,d[x])

        for i in range(len(s1)):
            if s1[i]>s2[i]:
                union(s1[i],s2[i])
            elif s2[i]>s1[i]:
                union(s2[i],s1[i])

        
        s=""
        for i in range(len(baseStr)):
            s+=find(baseStr[i])

        return s




