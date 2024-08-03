class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        check = Counter(target)
        check2 = Counter(arr)
        for num in arr:
            if check[num]!=check2[num] or num not in check:
                return False
        return True