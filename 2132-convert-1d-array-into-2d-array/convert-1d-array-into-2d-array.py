class Solution:
    def construct2DArray(self, original, m, n):
        if len(original) != m * n:
            return []

        ans = [[0] * n for _ in range(m)]

        for i in range(len(original)):
            ans[i // n][i % n] = original[i]

        return ans