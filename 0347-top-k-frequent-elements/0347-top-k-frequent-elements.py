class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # if len(nums)==k:
        #     return nums
        # arr=[]
        # freq= collections.Counter(nums)
        # reverse_dict = {}
        # for key, value in freq.items():
        #     reverse_dict[value] = key
        # # print(freq)
        # # print(reverse_dict)
        # freqList= freq.values()
        # newList=sorted(freqList,reverse=True)
        # # print(newList)
        # # print(reverse_dict[newList[0]])
        # for i in range (k):
        #     arr.append(reverse_dict[newList[i]])
        # return arr
        count, unique, c = [], [], []

        for i in nums:
            if i not in unique:
                unique.append(i)
                c.append(nums.count(i))

        for i in range(k):
            m=max(c)
            i=c.index(m)
            count.append(unique[i])
            c[i]=-1
        return count
        
        