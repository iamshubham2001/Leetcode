class Solution {
public:
    void rotate(vector<int>& nums, int k) {
       int n = nums.size();
       k = k % n;    // to varify the k is within the range [0,n] so use modulous

        // Reverse teh entire array
       reverse(nums.begin(),nums.end());

       // Reverse the first part [ first k element]
       reverse(nums.begin(), nums.begin() + k);

       // Reverse the second part [rest of the element after k]
       reverse(nums.begin() + k, nums.end());

       
    
    }

};