class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeros = []
        ones = []
        for chr in s:
            if chr=="0":
                zeros.append(chr)
            else:
                ones.append(chr)
        zeros.append(ones.pop())
        return "".join(ones + zeros)