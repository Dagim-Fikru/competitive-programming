class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumOfEven = 0
        ans = []
        for num in nums:
            if num%2==0:
                sumOfEven+=num
        for i in range(len(queries)):
            if nums[queries[i][1]]%2!=0:
                nums[queries[i][1]]= nums[queries[i][1]] + queries[i][0]
                if nums[queries[i][1]]%2==0:
                    sumOfEven+=nums[queries[i][1]]
            else:
                nums[queries[i][1]]+= queries[i][0]
                if nums[queries[i][1]]%2==0:
                    sumOfEven+=queries[i][0]
                else:
                    sumOfEven-= nums[queries[i][1]]-queries[i][0]
            ans.append(sumOfEven)
        return ans

