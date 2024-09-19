class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums)-1
        while s<=e:
            m = (s+e)//2
            if nums[m] < target:
                s = m+1
            elif nums[m] > target:
                e = m-1
            else:
                return m
        return s