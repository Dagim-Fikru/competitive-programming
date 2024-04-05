class TimeMap:

    def __init__(self):
        self.mapping = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not self.mapping[key]:
            return ""
        left = 0
        right = len(self.mapping[key])
        while right>left:
            mid = (right+left)//2
            if self.mapping[key][mid][1] < timestamp+1:
                left = mid+1
            else:
                right = mid
        return self.mapping[key][left-1][0] if self.mapping[key][left-1][1]<=timestamp else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)