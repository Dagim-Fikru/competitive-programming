class Solution:
    def baseNeg2(self, n: int) -> str:
        result = []
        
        while n:
            result.append('1' if n & 1 else '0')
            n = -(n >> 1)
        
        return ''.join(result[::-1]) if result else '0'