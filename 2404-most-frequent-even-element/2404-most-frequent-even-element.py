class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_nums = [num for num in nums if num % 2 == 0]
        if not even_nums:
            return -1
        freq_count = {}
        for num in even_nums:
            if num not in freq_count:
                freq_count[num] = 1
            else:
                freq_count[num] += 1
        max_freq = max(freq_count.values())
        most_frequent = min(num for num, freq in freq_count.items() if freq == max_freq)
        return most_frequent
        