# Problem: Add 1 to the number represented by ll
# Given the head of a singly linked list representing a positive integer number. Each node of the linked list represents a digit of the number, 
# with the 1st node containing the leftmost digit of the number and so on. The task is to add one to the value represented by the linked list 
# and return the head of a linked list containing the final value.

# The number will contain no leading zeroes except when the value represented is zero itself.

# Example 1:
# Input: head -> 1 -> 2 -> 3

# Output: head -> 1 -> 2 -> 4

# Explanation: The number represented by the linked list = 123.

# 123 + 1 = 124.

# Example 2:
# Input: head -> 9 -> 9

# Output: head -> 1 -> 0 -> 0

# Explanation: The number represented by the linked list = 99.

# 99 + 1 = 100.

# Approach: 
#         # reverse then No
#         #add 1 with carry
#         #reverse it again

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseNo(self, head):
        prev=node = None
        curr = head
        while curr:
            node = curr.next
            curr.next = prev
            prev = curr
            curr = node
        return prev

    def addOne(self, head):

        head = self.reverseNo(head)
        curr = head
        carry = 1

        while curr:
            curr.val += carry
            carr = curr.val //10
            curr.val %=10
            curr = curr.next

        head = self.reverseNo(head)

        # a new node for the carry
        if carry:
            node = ListNode(carry)
            node.next = head
            head = node

# COMPLEXITIES
# TIME:  O(N)
# SPACE: O(1)