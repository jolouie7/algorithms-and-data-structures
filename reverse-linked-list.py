#How to reverse a linked list in python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node = None
        curr_node = head
        next_node = None

        while curr_node:
          next_node = curr_node.next
          curr_node.next = prev_node
          prev_node = curr_node
          curr_node = next_node

        return prev_node


#Example
#Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
#Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
