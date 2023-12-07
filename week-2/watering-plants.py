class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        refill = capacity
        for i in range(len(plants)):
            if plants[i]<=capacity:
                steps+=1
                capacity-=plants[i]
            elif plants[i]>capacity:
                steps+= (2*i)+1
                capacity= refill
                capacity-=plants[i]
        return steps