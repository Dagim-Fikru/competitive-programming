class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = []
        while deck:
            if len(ans)>=2:
                ans.append(ans.pop(0))
            ans.append(deck.pop())
        return ans[::-1]
        
        