class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def First(nums,target):
            l = 0
            r = len(nums)-1
            first = -1
            while l<=r:
                m = l + (r-l)//2
                if nums[m] == target:
                    first = m
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return first

        def Last(nums, target):
            l = 0
            r = len(nums)-1
            last = -1
            while l<=r:
                m = l + (r-l)//2
                if nums[m]==target:
                    last = m
                    l = m+1
                elif nums[m]<target:
                    l=m+1
                else:
                    r = m-1
            return last

        first = First(nums,target)
        last = Last(nums,target)
        return(first,last)