class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count = 0;
        int scan = 0;
        while(scan<nums.size()){
            if(nums[scan] != val){
                nums[count] = nums[scan];
                count++;
            }
            scan++;
        }
        return count;
        
    }
};