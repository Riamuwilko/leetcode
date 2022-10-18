class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int counter = 1;
        int scan = 1;
        while(scan < nums.size()){
            if(nums[scan-1] != nums[scan]){
                nums[counter] = nums[scan];
                scan++;
                counter++;
            }
            else{
                scan++;
            }
            
        }
        return counter;
}
};