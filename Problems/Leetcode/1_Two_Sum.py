# https://leetcode.com/problems/two-sum/
# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store compliment and curr idx in dic
        # if we find the compliment in the dic, we return curr idx and val in dic
        
        dic = {}
        for i in range(len(nums)):
            # see if curr num is in dic
            if nums[i] in dic:
                return [i, dic[nums[i]]]
            # if not in dic then add the compliment and curr idx
            else:
                dic[target - nums[i]] = i