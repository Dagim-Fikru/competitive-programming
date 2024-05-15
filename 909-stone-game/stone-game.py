class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        even_sum = 0
        odd_sum = 0
        for _ in range(len(piles)):
            if _%2:
                odd_sum+=piles[_]
            else:
                even_sum+=piles[_]

        return True if even_sum > odd_sum else True
