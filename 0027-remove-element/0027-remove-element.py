class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0;
        scan = 0;
        while scan < len(nums):
            if nums[scan] != val:
                nums[count] = nums[scan]
                count += 1
            scan += 1
        return count