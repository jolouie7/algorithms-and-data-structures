# https://leetcode.com/problems/delete-node-in-a-linked-list/
# 237. Delete Node in a Linked List

# Write a function to delete a node(except the tail) in a singly linked list, given only access to that node.
# Given linked list - - head = [4, 5, 1, 9], which looks like following:
# 4 -> 5 -> 1 -> 9

# Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        if next_node:
          node.val = next_node.val
          node.next = next_node.next
        else:
          raise Exception("Can't use this thchnique to delete last node")
