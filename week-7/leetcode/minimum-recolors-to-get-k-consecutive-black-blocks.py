class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minNumOpr = len(blocks)
        CountFreq = Counter(blocks[:k])
        minNumOpr = min(minNumOpr,CountFreq['W'])
        for i in range(len(blocks)-k):
            CountFreq[blocks[i]]-=1
            CountFreq[blocks[i+k]]+=1
            minNumOpr = min(minNumOpr,CountFreq['W'])
        return minNumOpr

        