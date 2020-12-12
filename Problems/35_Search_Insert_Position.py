# https://leetcode.com/problems/search-insert-position/
# 35. Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# Example 1:
# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1, 3, 5, 6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1, 3, 5, 6], target = 7
# Output: 4

# Example 4:
# Input: nums = [1, 3, 5, 6], target = 0
# Output: 0

# Example 5:
# Input: nums = [1], target = 0
# Output: 0

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

      l = 0
      r = len(nums) - 1

      while l <= r:
        m = l + ((r - l) // 2)

        if nums[m] == target:
          return m

        if target < nums[m]:
          r = m - 1
        else:
          l = m + 1
      return l

      # [1,2,3,4], tar=3 ok
      # [1,4,6,7], tar=3 ok
      # [1,2,3,4], tar=5 ok
      # [1,2,3,4], tar=0 ok

      # Example from Leetcode
      # [1,3,5,6], tar=2
      # l = 0 + 1 = 1
      # r = 0
      # m = 0

      # time: o(log n)
      # space: o(1)
