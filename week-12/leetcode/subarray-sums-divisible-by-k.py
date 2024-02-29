class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cur = 0
        counter = Counter()
        for num in nums:
            cur = (cur + num) % k
            counter[cur] += 1
        ans = 0
        for i in counter:
            ans += counter[i]*(counter[i]-1)//2
        return ans + counter[0]