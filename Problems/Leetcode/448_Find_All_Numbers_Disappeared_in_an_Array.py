# 448. Find All Numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []

        new_nums = set(nums)

        for i in range(1, len(nums)+1):
            if not i in new_nums:
                result.append(i)

        return result

# Time: o(n), we have to go through each element in the nums list
# Space: o(n), we create a set of new_nums to take out any duplicates in the nums list