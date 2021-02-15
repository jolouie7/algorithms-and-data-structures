# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return False
        elif self.isSameTree(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, s, t):
        #if s is None make sure T is also None, return True
        if s == None and t == None:
            return True
        #if one is None and the other isn't return False
        elif s == None or t == None:
            return False
        #if they both have values see if they are the same vals
        elif s.val == t.val:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        else:
            return False

# Time: o(n)
# Space: o(n)