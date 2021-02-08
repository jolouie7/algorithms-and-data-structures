# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        return self.dfs(root, None, None)

    def dfs(self, root, min_node, max_node):
        if not root:
            return True

        if min_node != None and root.val >= min_node or max_node != None and root.val <= max_node:
            return False

        return self.dfs(root.left, root.val, max_node) and self.dfs(root.right, min_node, root.val)

# Time: O(N), because we have to touch every node
# Space: o(N), because we are using recursion