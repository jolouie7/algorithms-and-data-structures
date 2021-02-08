# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #dfs, post-order
        #we are just moving the pointers around
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        #swap
        root.left, root.right = right, left

        return root

# Time: O(N), because we need to touch every node in the tree
# Space: O(N), because of recursion