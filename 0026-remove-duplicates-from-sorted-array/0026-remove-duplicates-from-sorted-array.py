class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1;
        scanner = 1;
        while(scanner < len(nums)):
            if nums[scanner-1] != nums[scanner]:
                nums[count] = nums[scanner]
                count+=1
                scanner+=1
            else:
                scanner+=1
        return count