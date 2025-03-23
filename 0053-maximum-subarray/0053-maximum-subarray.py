class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, max1=0, -inf
        for c in nums:
            curr = max(c,curr+c)
            max1 = max(max1,curr)
        return max1