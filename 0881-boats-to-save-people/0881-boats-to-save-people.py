class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        # count=0
        # for i in range(len(people)):
        #     for j in range(i+1,len(people)-i):
        #         # if i==j:
        #         #     continue
        #         if people[i]>=limit or people[j]>=limit:
        #             count+=1
        #         elif people[i]+people[j]<=limit:
        #             count+=1
        i=0
        j=len(people)-1
        count = 0
        while i<=j:
            # if people[i]>=limit or people[j]>=limit:
            #     count+=1
            if people[i]+people[j]<=limit:
                i+=1
                j-=1
            else:
                j-=1
            count+=1
            # i+=1
            # j-=1
        return count
        
        