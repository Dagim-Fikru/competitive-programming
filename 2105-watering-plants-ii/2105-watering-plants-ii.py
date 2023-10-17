class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        arr=[0]*len(plants)
        a=capacityA
        b=capacityB
        A=0
        B=len(plants)-1
        if len(plants)%2==0:
            while A<B:
                if plants[A]<=capacityA:
                    capacityA-=plants[A]
                    A+=1
                else:
                    arr[A]+=1
                    capacityA=a
                    capacityA-=plants[A]
                    A+=1
                if plants[B]<=capacityB:
                    capacityB-=plants[B]
                    B-=1
                else:
                    arr[B]+=1
                    capacityB=b
                    capacityB-=plants[B]
                    B-=1
        else:
            while A<=B:
                if A==B:
                    if capacityA>capacityB:
                        if plants[A]<=capacityA:
                            capacityA-=plants[A]
                            A+=1
                        else:
                            capacityA = a
                            arr[A]+=1
                            A+=1
                    elif capacityA<capacityB:
                        if plants[A]<=capacityB:
                            capacityB-=plants[B]
                            B-=1
                        else:
                            capacityB = b
                            arr[B]+=1
                            B-=1
                    else:
                        if plants[A]<=capacityA:
                            capacityA-=plants[A]
                            A+=1
                        else:
                            arr[A]+=1
                            capacityA=a  
                            A+=1
                else:
                    if plants[A]<=capacityA:
                        capacityA-=plants[A]
                        A+=1
                    else:
                        arr[A]+=1
                        capacityA=a  
                        capacityA-=plants[A]
                        A+=1
        
                    if plants[B]<=capacityB:
                        capacityB-=plants[B]
                        B-=1
                    else:
                        arr[B]+=1
                        capacityB=b
                        capacityB-=plants[B]
                        B-=1
            
        print(arr)
        return sum(arr)
        
            
                