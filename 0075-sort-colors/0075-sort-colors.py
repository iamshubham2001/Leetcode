class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # use three pointer

        low = 0
        current = 0
        high = len(nums)-1

        while current <= high:
            if nums[current] == 0:
                nums[low],nums[current] = nums[current],nums[low]
                low +=1
                current +=1
            elif nums[current] == 1:
                current += 1
            else :
                nums[current],nums[high] = nums[high], nums[current]
                high -= 1


        