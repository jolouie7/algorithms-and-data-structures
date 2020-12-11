# 169. Majority Element
# https://leetcode.com/problems/majority-element/

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:
# Input: [3, 2, 3]
# Output: 3

# Example 2:
# Input: [2, 2, 1, 1, 1, 2, 2]
# Output: 2


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}

        #The only element in the list
        if len(nums) == 0:
          return nums[0]

        #add all the elements to hsh
        for num in nums:
          if num in dic:
            dic[num] += 1
          else:
            dic[num] = 1

        #loop through dic and find the current highest instance of num,
        #when you find a num with more instances, replace curr num and num_amt_val
        curr_num = None
        num_amt_val = None

        for k, v in dic.items():
          if num_amt_val == None:
            curr_num = k
            num_amt_val = v
          elif v >= num_amt_val:
            curr_num = k
            num_amt_val = v

        return curr_num