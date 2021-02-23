# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        #construct the root
        root_value = preorder.pop(0)
        root = TreeNode(root_value)
        index_value = inorder.index(root_value)

        #construct the left and right subTrees
        root.left = self.buildTree(preorder, inorder[:index_value])
        root.right = self.buildTree(preorder, inorder[index_value+1:])

        return root

# Time: O(N), Popping from the beginning of the list is linear time. Recursion is also linear time.
# Space: O(N), we have to build each node