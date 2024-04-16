class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==k:
            return nums
        frequency= Counter(nums)
        arr=[]
        arr2=[]
        for keys,values in frequency.items():
            arr.append([keys,values])
        arr=sorted(arr, key=lambda x: -x[1])
        for i in range(k):
            arr2.append(arr[i][0])
        # arr= list(set(sorted(nums, key=lambda x: (frequency[x], nums.index(x)))))
        return arr2
        
        
        