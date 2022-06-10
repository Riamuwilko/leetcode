class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numlist = {}
        for i in range(len(nums)):
            if nums[i] in numlist:
                return [numlist[nums[i]], i];
            else:
                numlist[target - nums[i]] = i
    
        