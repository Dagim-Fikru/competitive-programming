class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = n + 1
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        deque = collections.deque()
        for i in range(n + 1):
            while deque and prefix_sum[i] - prefix_sum[deque[0]] >= k:
                res = min(res, i - deque.popleft())
            while deque and prefix_sum[i] <= prefix_sum[deque[-1]]:
                deque.pop()
            deque.append(i)
        if res != n + 1:
            return res
        else:
            return -1
        
        