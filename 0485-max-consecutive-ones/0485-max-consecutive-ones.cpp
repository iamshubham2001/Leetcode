class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        // int n = nums.size();
        int count = 0;
        int ans = 0;
        for (int i:nums) {
            if (i==1) {
                count++;
            } else {
                count = 0;
            }
            ans = max(ans, count);
        }
        return ans;
    }
};