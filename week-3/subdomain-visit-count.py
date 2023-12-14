class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mapping = {}
        ans=[]
        for i in cpdomains:
            x=""
            indx = 0
            for j in i:
                if j==" ":
                    break
                x+=j
                indx+=1
            x = int(x)
            while indx!=-1:
                mapping[i[indx+1:]] = mapping.get(i[indx+1:],0) + x
                indx = i.find('.',indx+1,len(i)-1)
        for key,value in mapping.items():
            ans.append(str(value)+ " " + key)
        return ans
            # print(x,indx)
