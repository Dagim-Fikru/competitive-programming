class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mapping = defaultdict(list)
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j]==arr2[i]:
                    mapping[arr2[i]].append(arr1[j])
        arr=[]
        arr1.sort()
        for i in mapping:
            arr.extend(mapping[i])
        for i in arr1:
            if i not in arr2:
                arr.append(i)
        return arr
