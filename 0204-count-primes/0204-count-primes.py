class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True for i in range(n+1)]
        p = 2
        while p**2 < n:
            if prime[p]:
                for i in range(p**2, n+1, p):
                    prime[i] = False
            p += 1
        primes = [i for i in range(2, n) if prime[i]]
        return len(primes)
        