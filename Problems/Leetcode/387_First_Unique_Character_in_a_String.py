# https://leetcode.com/problems/first-unique-character-in-a-string/
# 387. First Unique Character in a String

# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

# Examples:
# s = "leetcode"
# return 0.

# s = "loveleetcode"
# return 2.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}

        for ele in s:
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1

        for k, v in dic.items():
            if v == 1:
                return s.index(k)
        return -1

# Time: o(n)
# Space: o(n)