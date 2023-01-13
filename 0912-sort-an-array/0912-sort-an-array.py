class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        max_element = int(max(nums))
        min_element = int(min(nums))
        range_of_elements = max_element - min_element + 1
        count_arr = [0 for _ in range(range_of_elements)]
        output_arr = [0 for _ in range(len(nums))]
        
        for i in range(0, len(nums)):
            count_arr[nums[i]-min_element] += 1
            
        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i-1]

        for i in range(len(nums)-1, -1, -1):
            output_arr[count_arr[nums[i] - min_element] - 1] = nums[i]
            count_arr[nums[i] - min_element] -= 1
            
        for i in range(0, len(nums)):
            nums[i] = output_arr[i]
        return nums
        
    
        