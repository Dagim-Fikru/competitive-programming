class Solution:
    def minSteps(self, n: int) -> int:
        Primefactors = []
        divisor = 2
        while divisor <= n:
            if n % divisor == 0:
                Primefactors.append(divisor)
                n = n / divisor
            else:
                divisor += 1
        return sum(Primefactors)