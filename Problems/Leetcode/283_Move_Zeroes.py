# https://leetcode.com/problems/move-zeroes/
# 283. Move Zeroes

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:
# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0

        while p2 < len(nums):
            if nums[p2] != 0:
                nums[p2], nums[p1] = nums[p1], nums[p2]
                p1 += 1
                p2 += 1
            else:
                p2 += 1

# Time: o(n)
# Space: o(1)