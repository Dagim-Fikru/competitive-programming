class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for i in range(len(nums)):
            if nums[i] not in mapping:
                mapping[nums[i]]=i
            else:
                if abs(mapping[nums[i]]-i)<=k:
                    return True
                else:
                    mapping[nums[i]]=i
        return False
            
            