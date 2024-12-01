class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0  # To store the maximum count of consecutive 1's
        current_count = 0  # To track the current streak of 1's

        for num in nums:
            if num == 1:
                current_count += 1  # Increment the current streak
                max_count = max(max_count, current_count)  # Update max if needed
            else:
                current_count = 0  # Reset the streak if a 0 is encountered
        return max_count