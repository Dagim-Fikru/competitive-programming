class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        arr2=[]
        set1=set(s)
        for c in set1:
            arr2.append(c)
        arr2.sort()
        alpha_dict = {char: index for index, char in enumerate(string.ascii_lowercase)}
        arr=[0]*26
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if i==j:
                    continue
                else:
                    if s[i]==s[j]:
                        arr[alpha_dict[s[i]]]=j-i-1
                        # arr.insert(alpha_dict[s[i]],j-i-1)
        # return arr[:alpha_dict[arr2[-1]]+1]== distance[:alpha_dict[arr2[-1]]+1]
        for i in arr2:
            if arr[alpha_dict[i]]== distance[alpha_dict[i]]:
                continue
            else:
                return False
        return True
                        
        