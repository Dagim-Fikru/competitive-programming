class Solution:
    def totalMoney(self, n: int) -> int:
        if n<7:
            return (n*(n+1))//2
        else:
            numOfWeeks = n // 7
            remainingDays = n % 7
            totalWeeks = 28 * numOfWeeks + 7 * (numOfWeeks - 1) * numOfWeeks // 2
            totalRemainingDays = (remainingDays * (remainingDays + 1)) // 2 + remainingDays * numOfWeeks
            total = totalWeeks + totalRemainingDays
        return total


           