class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        check = set()
        l=0
        minLength = float('inf')
        for r in range(len(cards)):
            if cards[r] in check:
                while cards[r] in check:
                    minLength = min(minLength,r-l+1)
                    check.remove(cards[l])
                    l+=1
            check.add(cards[r])
        return minLength if minLength!=float('inf') else -1