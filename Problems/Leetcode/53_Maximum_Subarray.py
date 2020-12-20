# https://leetcode.com/problems/maximum-subarray/
# 53. Maximum Subarray

# Given an integer array nums, find the contiguous subarray(containing at least one number) which has the largest sum and return its sum.
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Example 1:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [0]
# Output: 0

# Example 4:
# Input: nums = [-1]
# Output: -1

# Example 5:
# Input: nums = [-2147483647]
# Output: -2147483647

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force would be o(n^2) time, by iterating and finding each combination of subarrays

        if len(nums) == 1:
            return nums[0]

        global_max = curr_max = nums[0]

        for i in range(1, len(nums)):
            # always reassign curr_max
            curr_max = max(nums[i], curr_max + nums[i])

            if curr_max >= global_max:
                global_max = curr_max

        return global_max

# Time Complexity: o(n)
# Space Complexity: o(1)