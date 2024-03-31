class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def isPrime(n):
            primeNums = []
            is_prime = [True] * (n+1)
            is_prime[0] = is_prime[1] = False
            for p in range(2, int(n**0.5)+1):
                if is_prime[p]:
                    for i in range(p*p, n+1, p):
                        is_prime[i] = False
            for i in range(2, n+1):
                if is_prime[i]:
                    primeNums.append(i)
            return primeNums
        
        newArr = isPrime(n)
        ans = []
        # print(primeNums)
        i=0
        j=len(newArr)-1
        while i<=j:
            if newArr[i]+newArr[j] < n:
                i+=1
            elif newArr[i]+newArr[j] > n:
                j-=1
            else:
                ans.append([newArr[i],newArr[j]])
                i+=1
                j-=1
        return ans